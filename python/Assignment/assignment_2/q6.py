#calculate total salary of employee based on da,ta,hra of basic

basic=float(input("enter basic salary:"))

da=0.10*basic
ta=0.12*basic
hra=0.15*basic

total_salary=basic+da+ta+hra

print("total salary=",total_salary)