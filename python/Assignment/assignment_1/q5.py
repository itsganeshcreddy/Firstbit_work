#compound interest

p = float(input("Enter the principle amount = "))
t = float(input("Enter the time in year = "))
r = float(input("Enter the rate of intrest = "))

#simple Intrest
SI=(p*t*r)/100
print("simple intrest",SI)

#compound intrest
A=p*(1 +r/100)**t
CI=A-p
print("final amount = ",A)
print("compound intrest =",CI)