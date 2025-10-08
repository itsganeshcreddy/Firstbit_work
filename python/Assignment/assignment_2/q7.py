#sum of three digit number

num=int(input("enter three digit number:"))

a= num // 100
b= (num // 10)%10
c= num % 10

sum_digits=a+b+c

print("sum of digits=",sum_digits)