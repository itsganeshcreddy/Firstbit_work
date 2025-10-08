#swap num without third variable

a=int(input("enter first num:"))
b=int(input("enter second num:"))

print(f"before swapping,a is {a} &, b is {b}")

a,b=b,a

print(f"after swapping,a is {a} &, b is {b}")