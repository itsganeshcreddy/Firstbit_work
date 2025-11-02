# 3. Write a program to find sum of following series using functions : 
      # a. 1+ 2 + 3 + 4+….. + n 
      # b. 1!+ 2! + 3! + 4!+….. + n! 
      # c. 1^1 + 2^2 + 3^3+ …… n^n
      
#a.  1+ 2 + 3 + 4+….. + n 
def sum_series():
    n = int(input("Enter n: "))
    s = 0
    for i in range(1, n + 1):
        s = s + i
    print("Sum =", s)
    
sum_series()

#b. 1!+ 2! + 3! + 4!+….. + n!
def sum_factorial():
    n = int(input("Enter n: "))
    s = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        s = s + fact
    print("Sum =", s)

sum_factorial()

#c 1^1 + 2^2 + 3^3+ …… n^n 
def power_sum():
    n = int(input("Enter n: "))
    total = 0
    for i in range(1, n + 1):
        total += i ** i

    print("Sum =",total)
power_sum()




