'''request module is used to make  http request.in which we can use
get post put delete method as well'''



'''get request'''
# import requests
# responce = requests.get("https://www.google.com/")
# print(responce.text)


import requests
url = "https://www.python.org/"
r = requests.get(url)
print(r.text)


'''post request'''

# import requests
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : "vinod",
#     "body"  : "sarwade",
#     "userid" : "133"
# }
# headers = {
#     'content-type':'application/json;charset=UTF-8',
# }
# responce = requests.post(url,headers=headers,json=data)
# print(responce.text)






