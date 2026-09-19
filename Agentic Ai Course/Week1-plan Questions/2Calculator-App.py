# Write a Python Program to perform arithmetic calculations.

# Ask user to input two numbers and choice between following options

# Addition
# Subtraction
# Multiplication
# Division
# Calculate respective arithmetic and show desire output


a=int(input("Enter no :"))
b = int(input("Enter no :"))
while True:
    print("Choose one option of following : ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    ch = int(input("Enter Choice : "))

    if ch==1 :
        print("Addition of Numbers ",a,"and ",b," = ",(a+b))
    elif ch==2 :
        print("Subtraction of Numbers ",a,"and ",b," = ",(a-b))
    elif ch==3 :
        print("Multiplication of Numbers ",a,"and ",b," = ",(a*b))
    elif ch==4 :
        print("Division of Numbers ",a,"and ",b," = ",(a/b))
    elif ch==5 :
        print("Exit")
        break
    else :
        print("Invalid Choice")
    