print("Calculator v0.1")
print("©All rights reserved by Omeriko436 INC.")
print(" ")
print("Enter the following calculation.")
c = input("1 For +, 2 for -, 3 for x and 4 for /.")
a = int(input("Enter the first number.")) #I made this whit int() because unless I do this it will just
b = int(input("Enter the second number.")) #make the numbers next to them.

if c == "1": #Addion
    r=a+b

elif c == "2": #Subtraction
    r=a-b

elif c == "3": #Multiplication
    r=a*b

elif c == "4": #Divide
    r=a/b

else: #Wrong enter
    print("You entered a wrong character. Please try again later.")
    exit

print(r)
