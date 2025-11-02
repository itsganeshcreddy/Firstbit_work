# 4. Sum of all odd numbers between 1 to n 

def sum_odd():
    n = int(input("Enter n: "))
    s = 0
    for i in range(1, n + 1):
        if (i % 2 != 0):
            s = s + i
    print("Sum of odd numbers =", s)
sum_odd()
