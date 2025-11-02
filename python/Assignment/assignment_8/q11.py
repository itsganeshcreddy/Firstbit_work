# 11. WAP to check if a given number is Armstrong number or not. For 
# each task create separate functions.

def armstrong():
    num = int(input("Enter a number: "))

    temp = num
    count = len(str(num))  
    sum = 0
    while(temp > 0):
        d = temp % 10
        power = 1

        for i in range(count):
            power *= d
        sum += power
        temp //= 10
    if(sum == num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
armstrong()