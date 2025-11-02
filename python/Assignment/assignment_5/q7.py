#7. Write a program to print first n prime numbers. 

n= int(input("How many frist prime number number you want number :-"))
count = 0
num = 2
while(count < n):
    for i in range(2, num):
        if(num % i == 0):
            #print(f'{num} not a prime number.')
            break
    else:
        #print(f'{num}is a prime number.')
        print(num, end = ' ')
        count +=1
    num +=1