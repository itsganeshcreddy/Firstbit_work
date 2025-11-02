# 10.WAP to check if given number is Perfect Number.
  
# sum of divisors (excluding n) == n
# A perfect number is a positive integer that is equal to
# the sum of its proper divisors (excluding the number itself).

num = int(input("Enter a number: "))

sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
