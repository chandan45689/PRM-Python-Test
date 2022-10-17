# # Triangle Validation
a=int(input("The first Side:"))
b=int(input("The second Side:"))
c=int(input("The third Side:"))
if all([a+b > c, b+c > a , c+a > b]):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#Rectangle Validation

s=int(input("Enter the side:"))
adjacent_of_s=int(input("Enter the adjacent side:"))
p=int(input("Enter the side:"))
adjacent_of_p=int(input("Enter the adjacent side:"))
if all([s==p,adjacent_of_s==adjacent_of_p]):
    print("Validate Rectangle")
else:
    print("Invalid Rectangle")
