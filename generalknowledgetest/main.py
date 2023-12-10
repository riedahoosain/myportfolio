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
    if user_choice == question["correct_answer"]:
        print("correct answer")
        score = score + 1
    else:
        print("incorrect answer")

for index, question in enumerate(data):
    message = f"{index + 1} - Your answer: {question['user_choice']}, " \
              f"Correct Answer: {question['correct_answer']}"
    print(message)
#print(data)
print(f"{score}  /  {len(data)}")