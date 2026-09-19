'''Write a program to classify a student’s grade based on marks with nested conditions:
Marks ≥ 90 → "Excellent"
Marks between 75–89 → "Good"
Marks between 50–74 → "Average"
Marks < 50 → "Fail"
Add a condition to check if marks are negative or above 100 (invalid input).
'''

m=int(input("Enter Marks :"))

if m >= 90:
    print("Excellent")
elif 75 < m > 89 :
    print("Good")
elif 50 < m > 74 :
    print("Average ")
elif m < 50 :
    print("Fail")
elif m < 0 or m > 100 :
    print("Invalid Input ")
