# WAP to calculate the sum of following series where n is input by user.
# 1/1! + 2/2! + 3/3! + ... N/N!

n = int(input("Enter the series number : "))
            
sum_series = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j               # fact = fact * j
    sum_series += i / fact

print("Sum of factorial series:", sum_series)