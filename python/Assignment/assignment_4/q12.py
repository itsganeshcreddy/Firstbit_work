#12. WAP to print Armstrong number within a given range
# An Armstrong number (also called a narcissistic number) is a number
# that is equal to the sum of its digits each raised to the power of the number 
# of digits.

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    temp = num
    count = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10

        power = 1
        for i in range(count):
            power = power * digit


        sum += power
        temp //= 10

    if sum == num:
        print(num)
