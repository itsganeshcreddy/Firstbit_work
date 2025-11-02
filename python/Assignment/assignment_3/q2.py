#check vowel or consonent

# Do not enter number
# Do not enter more than one character
alp=input("Enter an alphabet only :") 

if('a' <= alp <='z') or ('A' <= alp <='Z'):
    if(alp =='a' or alp =='e' or  alp =='i' or  alp =='o' or  alp =='u' or  alp =='A' or  alp =='E' or
        alp =='I' or  alp =='O' or  alp =='U'):
        print("It is a vowel.")
    else:
        print("It is consonent.")
else:
    print("It is not an alphabet.")            