'''Build a program that checks if a person is eligible for a loan:

Age ≥ 21

Salary ≥ 25,000

Credit score ≥ 700

Nested condition: If salary is less than 25,000 but credit score ≥ 800, still eligible.'''

age=int(input("Enter your Age :"))
sal=int(input("Enter your Salary :"))
score = int(input("Enter Your Credit score :"))

if age >= 21:
    if sal >=25000 and score >=700 :
        print("You are Eligible for loan...")
    elif sal < 25000 and score >=800:
        print("You are Eligible for loan...")
    else:
        print("You are not Eligible for loan...")
        
else:
    print("You are not Eligible for loan...")
    
