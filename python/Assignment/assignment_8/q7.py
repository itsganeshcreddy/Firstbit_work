# 7. Write a program to find sum of digits of a number.

def sum_digits_number():
    num = int(input("Enter a number: "))
    sum = 0

    while (num != 0):
        a = num % 10
        num = num // 10
        sum += a 
    print("Sum of digits =", sum)
sum_digits_number()