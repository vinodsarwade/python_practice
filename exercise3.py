#KBC Game

questions = [
    ["which language was used to create facebook ?","pyhton","c++","Javascript","java",1],
    ["which language was used to create whatsapp ?","pyhton","c++","Javascript","java",2],
    ["which language was used to create instagram ?","pyhton","c++","Javascript","java",3],
    ["which language was used to create chatgpt?","pyhton","c++","Javascript","java",4],
    ["which language was used to create pubg ?","pyhton","c++","Javascript","java",3],
    ["which language was used to create zerodha ?","pyhton","c++","Javascript","java",2],
    ["which language was used to create kotak ?","pyhton","c++","Javascript","java",1],

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,100000]
money = 0

for i in range(0,len(questions)):
    Question = questions[i]
    print(f"question for price{levels[i]}\n")

    print(f"Question : {Question[0]}")
    print(f"a.{Question[1]}       b.{Question[2]}")
    print(f"c.{Question[3]}       d.{Question[4]}")

    user_responce = int(input("enter your answer between(1 to 4):"))
    if user_responce == Question[-1]:
        print(f"Correct answer, you have won rs {levels[i]}\n")
        if (i ==3 ):
            money = 5000
        elif(i == 5):
            money = 20000
    else:
     print("wrong answer")
     break
print(f"your take home money is {money}")
    

