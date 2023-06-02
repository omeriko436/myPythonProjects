print("Calculator by omeriko436")
print(" ")
print("Enter the following calculation.")
c = input("1 For +, 2 for -, 3 for x and 4 for /.")
a = int(input("Enter the first number.")) #I wrote this code with the "int()" command because if I didn't,
b = int(input("Enter the second number.")) # it would just write the numbers side by side.

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

input(" ")
