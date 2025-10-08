#reverce num three digit

num=int(input("enter three digit num:"))

rev=(num%10)*100 + ((num//10)%10)*10 +(num//100)

print("Reversed number=",rev)
