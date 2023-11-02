import random

goa_family = ["luka", "nika", "gabrieli", "dato", "mari"]
questions_and_answers = {
    "11*11?" : 121,
    "121+26?": 147,
    "12/4?"  :  3,
    "77/11?" :  7,
    "56-37?" : 19,
    }

for i in range(len(goa_family)):
    student = random.choice(goa_family)
    st_question = random.choice(list(questions_and_answers.keys()))
    print(f"{student}, answer the question, {st_question}")

    goa_family.remove(student)
    

    answer = int(input("Enter the answer: "))
    correct_answer = questions_and_answers.get(st_question)

    
    if answer  == correct_answer :
        print("shen dagericxa 10 qula")
    else:
        print("shen chamogechra 5 qula")
