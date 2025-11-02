#9. WAP to print all numbers in a range divisible by a given number. 

lower = int(input("Enter the lower range : "))
upper = int(input("Enter the upper range : "))
divisor = int(input("Enter the number to check divisibility: "))


for i in range(lower, upper + 1):
    if i % divisor == 0:
        print(i, end=" ")
print(f" These numbers divisible by {divisor} between {lower} and {upper}.")