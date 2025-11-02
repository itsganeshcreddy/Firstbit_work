# 5. Sum of all prime numbers between 1 to n

def sum_prime_number():
    n = int(input("Enter n: "))
    s = 0

    for i in range(2, n + 1):
        for j in range(2, i):
            if(i % j == 0):
             break
        else:
          s = s + i

    print("Sum of prime numbers =",s)
sum_prime_number()