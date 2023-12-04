'''
text = input("Enter a title: ")
length = len(text)
print(f"length of title is {length}")
'''

#This is just a temp space I will add or test things before adding to my programs
#This is also use to scribble temp info and code

'''
contents = ["Clean the bin", 
            "Wash the car", 
            "Mop the Floor"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    with open(f"files/{filename}", 'w') as file:
        file.write(content)
'''

###################################################

'''
create a program that:

1. prompts the user to enter a new member.

2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.

In the above example, Solomon Right will be added to members.txt updating the content of the file to:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right



user_input = input("Add a new member: ")
with open("files/members.txt", 'r') as file:
    members = file.readlines()
members.append(user_input + "\n")

with open("files/members.txt", 'w') as file:
    file.writelines(members)
    file.close()

'''

#########################################################


    
'''

Open your computer IDE and place the following in a Python file:

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

Then, create a program that:

1. generates multiple text files by iterating over the filenames list,

2. and writes the text Hello  inside each generated text file.



filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(f"files/{filename}", 'w') as file:
        file.write("Hello")

'''


'''
Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

Then, create a program that:

1. reads each text file and

2. prints out the content of each file in the command line.

The expected output would be like the following:



filenames = ['a.txt', 'b.txt', 'c.txt'] 

for filename in filenames:
    with open(f"files/{filename}", 'r') as file: # Files are in a subdir called files
          content = file.read()
          print(content)

'''