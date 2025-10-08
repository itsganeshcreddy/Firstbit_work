#percentage of student on marks

s1=int(input("enter the  mark of s1="))
s2=int(input("enter the  mark of s2="))
s3=int(input("enter the  mark of s3="))
s4=int(input("enter the  mark of s4="))
s5=int(input("enter the  mark of s5="))

total_mark=s1+s2+s3+s4+s5
print("total marks=",total_mark)

per=(total_mark/500)*100
print("percentage=",per)