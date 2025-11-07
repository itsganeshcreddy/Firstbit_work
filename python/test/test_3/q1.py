# WAP to print first n prime numbers.

n = int(input("How many first prime number you want to : "))
count = 0
num = 2
while(count < n):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end = ' ')
        count += 1 
    num += 1       