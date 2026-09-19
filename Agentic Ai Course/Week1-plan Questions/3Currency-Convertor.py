# Write a Python Program to input Currency Amount in Indian Rupee and Convert to following Currency notes.

# US Doller
# Pounds
# Euros
# AU Doller
# Ask user to enter amount in INR and choice one of the option listed to convert to respective currency note. Show desired output to user.

i=int(input("Enter Amount in INR : "))
while True:
    print("Choose one option to convert INR into respective Currency :")
    print("1.US Doller")
    print("2.Pounds")
    print("3.Euros")
    print("4.AU Doller")
    print("5.Exit")
    ch = int(input("Enter Choice : "))
    if ch==1 :
        print("Amount in US Doller : ",(i*0.0104))
    elif ch==2 :
        print("Amount in Pounds : ",(i*0.0078))
    elif ch==3 :
        print("Amount in Euros : ",(i*0.0091))
    elif ch==4 :
        print("Amount in AU Doller : ",(i*0.015))
    elif ch==5 :
        print("Exit")
        break
    else :
        print("Invalid Choice")