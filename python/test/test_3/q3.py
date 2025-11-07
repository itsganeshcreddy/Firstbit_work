# WAP to accept basic salary of n emp.(n should be accepted from user).If basic salary below 20000 then
# da=10%,ta=12% and hra=15% Otherwise da=15%,ta=18% and hra=20%.
# Based on this calculate the total salary of each emp and also total salary of emp.

n = int(input("Enter number of employees : "))

total_all = 0

for i in range(1, n + 1):
    print("Employee",i)
    basic = float(input("Enter basic salary : "))

    if(basic < 20000):
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total = basic + da + ta + hra

    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total salary of employee", i, "=", total) 

    total_all += total

print("\nTotal salary of all employees =", total_all)     



