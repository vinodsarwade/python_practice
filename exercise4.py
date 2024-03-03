#secret code encoding and decoding
#if string has 3 or less than 3 word then reverse that string 
#if string has more than 3 words then append first letter to end of string ex: vinod -> inodv
#after appending it add 3 random char at start and end of string
# and last your program should ask decode also,if u want to decode

st = input("enter a message: ")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding : ")
coding = True if (coding == "1") else False
print(coding)
if(coding):                                             #encode
    newwords = []
    for word in words :
        if(len(words)>=3):
            r1= "dsf"
            r2 = "gfv"
            stnew = r1+word[1:]+word[0]+r2   #it will add r1 at start and then append first letter to end and then at last add r2
            newwords.append(stnew)
        else:
            newwords.append(word[:-1])   # it will reverse the string 
    print(" ".join(newwords))
else:                                                   #decode
    newwords= []
    for word in words:
        if (len(word)>=3):
            stnew = word[3:-3]   #remove first and last 3 words
            stnew = stnew[-1]+stnew[:-1] #last letter add to start and then remaining slice from 0 to -1
            newwords.append(stnew)
        else:
            newwords.append(word[:-1])
    print(" ".join(newwords))