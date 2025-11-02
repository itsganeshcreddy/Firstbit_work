#  check if given 3 digit number is a palindrome or not.

num = int(input("Enter 3 digit number:"))

n1 = num // 100
n2 = (num // 10) % 10
n3 = num % 10

if(n1 == n3):
    print(f'{num} is a palindrome.')
else:
    print(f'{num} is not a palindrome.')    