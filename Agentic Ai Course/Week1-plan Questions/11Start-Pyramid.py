'''Create a program that generates a pyramid of stars (*) with height given by the user.'''

n=int(input("Enter height :"))
p="*"
for i in range(1,n+1):
    print(p*i)
