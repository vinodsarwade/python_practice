Questions = [
    {"question":"eligible age for voting: ", "answer":"18","price":"1000"},
    {"question":"age for retired:", "answer":"58","price":"2000"},
    {"question":"capital of india:", "answer":"delhi","price":"3000"}
]

for i in Questions:
    question = i["question"]
    correct_answer = i["answer"]
    Price = i["price"]

    user_input = input(question+ " ")
    
    if user_input == correct_answer:
        print("answer is correct")
        print("you won rs:",Price)
        print("you are eligible for next question")
    else:
        print("failed")
        print("you answered wrong correct answer is:",correct_answer)
        break