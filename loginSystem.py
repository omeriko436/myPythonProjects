usnm="omeriko436" #username
pasw="omeriko436" #password
print("Login System by omeriko436")
print(" ")
ent1=input("Enter your username.") #Takes the entered value for username.
ent2=input("Enter your password.") #Same for password.

if ent1 == usnm:
    if ent2 == pasw:
        print("You have sucsessfully entered in.")
    else:
        print("Your password is wrong.")
else:
    print("You entered a wrong username.")
