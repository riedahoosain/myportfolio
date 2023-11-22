#This is just a temp space I will add or test things before adding to my programs
#This is also use to scribble temp info and code

contents = ["Clean the bin", 
            "Wash the car", 
            "Mop the Floor"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
   