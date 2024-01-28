import json
import os
from datetime import datetime
import time

import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import colorsys
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_perception_modules.armtag import InterbotixArmTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
import numpy as np
print('imports complete')
env_var = os.environ

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# determines the color of each object using the Hue value in the HSV color space
def color_compare(rgb):
    r,g,b = [x/255.0 for x in rgb]
    print(rgb)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    print(h,s,v)

    if h < 0.025: color = "red"
    elif 0.025 < h < 0.05: color = "orange"
    elif 0.1 < h < 0.15: color = "yellow"
    elif 0.2 < h < 0.48: color = "green"
    elif 0.5 < h < 0.55: color = "blue"
    elif 0.75 < h < 0.85: color = "purple"
    else: color = "unknown"
    
    print("found", color)
    return color


@app.route('/')
def upload_form():
    return 'reached!'
    return color

@app.route('/Status',methods=["GET"])
def Bot_Status():
    global status
    response_data = {
        'status': status,
        'message': 'operation started '
        }
    return jsonify(response_data), 200

@app.route('/Home_Pose',methods=["GET"])
def Home_Pose():
    global status
    bot.arm.go_to_home_pose()
    status = "Home_Pose"
    return "HomePose Initialized"

@app.route('/Sleep_Pose',methods=['GET'])
def Sleep_Pose():
    global status
    bot.arm.go_to_sleep_pose()
    status = "Sleep_Pose"
    return "Sleep Pose Initialized"



@app.route('/place/<color_select>/<drop_select>', methods=["GET"], defaults={'drop_select': 'z1'})
def tester(color_select, drop_select):
    # print('reached with: {} in {}'.format(color_select))
    return 'reached with: {} in {}'.format(color_select, drop_select)


@app.route('/get/colors', methods=['GET'])
def get_colors():
    success, clusters = pcl.get_cluster_positions(ref_frame="wx200/base_link", sort_axis="y", reverse=True)
    clr = []
    for cluster in clusters:
        x, y, z = cluster["position"]
        clr.append(color_compare(cluster["color"]))
    return jsonify(clr)


@app.route('/pick/<color_select>/<drop_select>', methods=['GET'])
def pick_colors(color_select, drop_select):
    global status
    status = "Picking_Object"
    zones = {"z1": {"x": 0.22, "y": 0.1},
    "z2": {"x": 0.22, "y": 0.2},
    "z3": {"x": 0.32, "y": 0.1},
    "z4": {"x": 0.32, "y": 0.2}
    }
    success, clusters = pcl.get_cluster_positions(ref_frame="wx200/base_link", sort_axis="y", reverse=True)
    clr = []
    bot.arm.set_ee_pose_components(x=0.3, z=0.2, moving_time=0.8, accel_time=0.4)
    for cluster in clusters:
        x, y, z = cluster["position"]
        clr = color_compare(cluster["color"])
        if (color_select == 'all'):
            x, y, z = cluster["position"]
            bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.1, pitch=0.5, moving_time=1.2, accel_time=0.6)
            bot.arm.set_ee_pose_components(x=x, y=y, z=z-0.05, pitch=0.5)
            bot.gripper.close()
            status="Picked"
            time.sleep(1)
            bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.2, pitch=0.5)   # after picking up it will raise upto certain distance
            print("1")
            bot.arm.set_ee_pose_components(x=x, y=-y, z=z+0.2, pitch=0.5)   # now arm will move to left side by -y - 0.2
            print(y)
            print("2")
            bot.arm.set_ee_pose_components(x=x, y=-y, z=z+0.5, pitch=0.0)   # now from here it will raise by z + 0.5
            print("3")
            bot.arm.set_ee_pose_components(x=x, y=-y, z=z+0.5, pitch=0.0)     #left 
            print("4")
            # bot.arm.set_ee_pose_components(x=x, y=-y, z=z+0.5, pitch=0.5)    #pitch up and  drop
            # print("5")
            time.sleep(1)
            bot.gripper.open()
            status= "Droped"
            # bot.arm.set_ee_pose_components(x=x, y=-y, z=z+0.5, pitch=0.5) #
            print('dropped at:', x, -y)
        else:
            print(drop_select)
            drop_zone = zones[drop_select]

            bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.1, pitch=0.5, moving_time=0.8, accel_time=0.4)
            if (clr == color_select):
                bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
                bot.gripper.close()
                bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.2)
                bot.arm.set_ee_pose_components(x=drop_zone['x'], y=drop_zone['y'], z=z+0.2, pitch=0.5)
                bot.arm.set_ee_pose_components(x=drop_zone['x'], y=drop_zone['y'], z=z, pitch=0.5)
                bot.gripper.open()
                bot.arm.set_ee_pose_components(x=drop_zone['x'], y=drop_zone['y'], z=z+0.2)
                # bot.arm.set_ee_pose_components(x=0.3, z=0.2)
            else:
                bot.arm.set_single_joint_position("wrist_rotate", -(np.pi/5), moving_time=0.6)
                bot.arm.set_single_joint_position("wrist_rotate", (np.pi/5), moving_time=0.6)
                bot.arm.set_single_joint_position("wrist_rotate", -(np.pi/5), moving_time=0.6)
    bot.arm.set_ee_pose_components(x=0.3, z=0.2, moving_time=1.2, accel_time=0.6)
    bot.arm.go_to_home_pose()
    status = "Home_Pose"
    return jsonify("All DONE!")


if __name__ == "__main__":
    bot = InterbotixManipulatorXS("wx200", moving_time=1.2, accel_time=0.6)
    pcl = InterbotixPointCloudInterface()
    status = "Sleep_Pose"
    armtag = InterbotixArmTagInterface()
    app.run(host='0.0.0.0', port='5123')
