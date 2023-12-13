#Create Jorunal entries to .txt file named the date


date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10: ")
thoughts = input("Let your thoughts flow:\n") 

with open(f'journal/{date}.txt', 'w') as file:

    file.write(mood + 2 * '\n') #Save List to File with added items
    file.write(thoughts)