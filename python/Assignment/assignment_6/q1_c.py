# 1.c

#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 

n = int(input("Enter number of rows: "))

for i in range(n):
    # Print spaces
    print(" " * (n - i), end=" ")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

     
