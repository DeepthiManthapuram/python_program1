p=int(input("enter principal amount:"))
t=int(input("enter no of months:"))
r=int(input("enter rate of interest:"))
s = (p*t*r)/100
print("simple interest=",s)
amount = p+s
print("amount in hands=",amount)