#11. WAP to check if given number Strong Number.

# A Strong Number is a number in which
# the sum of the factorials of its digits 
# is equal to the number itself.

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

for i in str(num):
    digit = int(i)
    fact = 1
    for j in range(1, digit + 1):
        fact *= j
    sum_fact += fact

if sum_fact == temp:
    print(temp, "is a Strong Number")
else:
    print(temp, "is not a Strong Number")