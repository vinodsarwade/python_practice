# f = open('main2.txt','w')
# lines = ['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()


f = open('main2.txt','w')
lines = ['line1','line2','line3']
for i in lines:  #for new line we can write like this also using for loop
    f.writelines(i + '\n')
    print(i)
f.close()

