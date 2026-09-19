'''Create a program to determine if a given year is:

Leap year

Century year

Special year (divisible by 400)

Invalid year (negative input).'''

y=int(input("Enter Year :"))

if y % 4 == 0 :
    print(y," is leap Year.")
elif y % 100 == 0 :
    print(y, " is Century Year.")
elif y % 400 == 0 :
    print(y, " is Special year.")
elif y < 0 :
    print("Invalid Input.")
else :
    print("Nothing Special year ")
    
    
