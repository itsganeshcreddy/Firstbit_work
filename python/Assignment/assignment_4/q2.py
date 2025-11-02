#2. WAP to print all odd numbers until n. 

n = int(input("Enter the value n : "))
i=n
print("odd number :")
for i in range(1, n + 1, 2):
    print(i)