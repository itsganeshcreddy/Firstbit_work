# 1.d

#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 

for i in range(1,6):
    x = i
    for j in range(1,6 - i):
        print(" ",end =" ")
    for j in range(1,i + 1):
        print(x, end =" ")
        x+=1
    x -= 2

    for j in range(1,i):
        print(x,end =" ")
        x -= 1

    print()