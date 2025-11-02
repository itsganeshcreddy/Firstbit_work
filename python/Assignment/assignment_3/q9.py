# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1=int(input("enter the  mark of s1="))
s2=int(input("enter the  mark of s2="))
s3=int(input("enter the  mark of s3="))
s4=int(input("enter the  mark of s4="))
s5=int(input("enter the  mark of s5="))

total_mark = s1 + s2 + s3 + s4 + s5
print("total marks:",total_mark)
per = (total_mark/500)*100
print("percentage:",per)

if(per >= 90 ):
    print("Outstanding...!!!")
elif(per >= 75 ):
    print("First class...")   
elif(per >= 60 ):
    print("Second class...")  
elif(per >= 35 ):
    print("Third class...")  
else:
    print("Fail...")              