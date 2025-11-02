#5. WAP to print Fibonacci series upto n. 

n = int(input("Enter how many terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

    