#in file handling we can handle opeartion on files,like open file read ,write ,delete, rename
# syntax is "fileName" ,"mode"

#if the file is exist then only it can open file otherwise throw error.
#READ MODE
f = open('main.txt','r')
# f = open('main.txt','rb')  #if wrote like rb means read in binary mode
text = f.read()
print(text)
f.close()

# WRITE MODE
f= open('main.txt','w')
f.write("hello all")
f.close()


#APPEND MODE
f= open('main.txt','a')
f.write("hello all ")
f.close()


# if we wrote like this we dont need to close file using "with open"
with open('main.txt','a') as f:
    f.write("hey am vinod")