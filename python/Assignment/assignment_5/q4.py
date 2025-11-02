# 4. Write a program to check if given number is Armstrong number or not.  
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  4*4*4*4)

num = int(input("Enter a number: "))

temp = num
count = len(str(num))  
sum = 0

# Loop to find sum of powered digits
while temp > 0:
    d = temp % 10

    power = 1
    for i in range(count):
        power *= d

    sum += power
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
