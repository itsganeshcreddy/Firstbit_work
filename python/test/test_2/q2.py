# 2.WAP to accept three digit number . if first digit is double of second digit and half of third digit,then display "yes,you have done it" otherwise display "please try next time"

num = int(input("Enter a number:"))
third = 0

if(100 <= num <= 999):
    first = num // 100
    second =(num // 10) % 10
    if(first == 2 * second):
        print("Yes, you have done it.")
    else:
        print("please try next time.")    
else:
    print("Please enter three digit number only...")    