#8. Write a program to solve the following series : 

#a. 1! + 2! + 3! + 4! + …..n! 
n = int(input("Enter value of n: "))
sum_fact = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum_fact += fact

print("Sum of factorial series:", sum_fact)

#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 

n = int(input("Enter value of n: "))
sum_pow = 0

for i in range(1, n + 1):
    sum_pow += n ** i

print("Sum of power series:", sum_pow)

#c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 
n = int(input("Enter number of terms: "))
sum_geo = 0
term = 1

for i in range(1, n + 1):
    sum_geo += term
    term *= 2  
print("Sum of geometric series:", sum_geo)

#d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 
a = float(input("Enter value of a: "))
sum_series = 0

for i in range(1, 11):
    sum_series += (a ** i) / i

print("Sum of series S:", sum_series)

#e. x - x2/3 + x3/5 - x4/7 + …. to n terms

x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
sum_series = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum_series += sign * (x ** i) / den
    sign *= -1      
    den += 2        

print("Sum of the series:", sum_series)
