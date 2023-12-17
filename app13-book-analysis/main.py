import re
with open("miracle_in_the_andes.txt","r", encoding='utf-8') as file:
    book = file.read()
pattern = re.compile("Chapter [a-z]") #looks for words that has chapter and letters eg Chapter a or Chapter b etc
pattern = re.compile("Chapter [0-9]+") #looks for words that has chapter and a number
finding = re.findall(pattern,book)
print(len(finding))