# find root of quardatic equation

a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))

root1=(-b + (b**2-4*a*c)**0.5) /2*a
root2=(-b + (b**2-4*a*c)**0.5) /2*a

print(f"root of given equation is {root1} & {root2}")