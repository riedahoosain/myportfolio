'''
A Questions and Answers app that reads from json file 
that asks user multiple choice questions and shows scores and answers

The File can have more multiple questions

'''

import json


def extractdata():
    with open("questions.json", 'r') as file:
        content = file.read()
    data_local = json.loads(content)
    return data_local


data = extractdata()
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        result = "Correct answer"
        score = score + 1
    else:
        result = "Incorrect answer"

    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
        f"Correct Answer: {question['correct_answer']}"
    print(message)
# print(data)
print(f"{score}  /  {len(data)}")
