# 6. Write a program to find print the following Fibonacci series using 
# functions:  1  1  2  3 5 8  n terms

def fibonacci():
    n = int(input("Enter number of terms: "))
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
fibonacci()



