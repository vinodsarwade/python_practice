'''shutil is a python built in module that provides higher leval interface for working with files and directories.
the name shutil is short for shell utility. it provides a convenient and efficient way to automate task that are commanly performed on files and directory.'''

# import shutil
# import os
# cwd = os.getcwd()
# print(cwd)
# source_file = os.path.join(cwd,"exercise.py")
# destination_file = os.path.join(cwd,"Code_with_harry.py")
# shutil.copy(source_file,destination_file)

'''1 : shutil.copy(source , destination)'''
# import shutil
# shutil.copy("exercise.py", "sh_module_cpoy.py")


'''2 : shutil.copy2'''
# import shutil
# shutil.copy2("exercise.py", "sh_module_cpoy.py")


'''3 : shutil.copytree''' #for folders not file
# import shutil
# shutil.copytree(".OOPS", "opps2")


'''3 : shutil.move'''
import shutil
shutil.move(".loops_/range.py", "range.py")







