'''Problem Statement: Calculate electricity bill based on units consumed.

Inputs & Conditions:
Input: Units consumed (integer).

Conditions:

≤ 100 units → ₹5 per unit
101–200 units → ₹7 per unit
200 units → ₹10 per unit

Expected Output: Total bill amount.'''

unit = int(input("Enter units consumed :"))

if unit <=100 :
    print("Total bill amount : ",unit*5)
elif unit >=101 and unit < 200 :
    print("Total bill amount : ",unit*7)
elif unit >= 200 :
    print("Total bill amount : ",unit*10)

