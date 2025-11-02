# 8. Write a program find reverse of a number 

def reverse():
    num = int(input("Enter a number: "))
    rev = 0

    while num > 0:
        digit = num % 10      
        rev = rev * 10 + digit  
        num = num // 10         

    print("Reverse of the number is:", rev)
reverse()