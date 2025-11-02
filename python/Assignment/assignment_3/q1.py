# Check given number positive or negative

num = int(input("Enter number:"))
if(num==0):
    print(f'{num} is a neutral number.')
elif(num>0):
    print(f'{num} is positive number.')
else:
    print(f'{num} is a negative number.')