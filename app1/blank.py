#This is just a temp space I will add or test things before adding to my programs
#This is also use to scribble temp info and code

length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")