# 11.Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
#       a. Children below 12 = 30% discount 
#       b. Senior citizen (above 59) = 50% discount 
#       c. Others need to pay full.

person1 = int(input("Enter the person1 age : "))
person2 = int(input("Enter the person2 age : "))
person3 = int(input("Enter the person3 age : "))
person4 = int(input("Enter the person4 age : "))
person5 = int(input("Enter the person5 age : "))

amount = int(input("Ticket price : "))
total = 0

if(person1<=12):
    total+=amount-(amount*0.3)
elif(person1>59):
    total+=amount-(amount*0.5)
else:
    total+=amount

if(person2<=12):
    total+=amount-(amount*0.3)
elif(person2>59):
    total+=amount-(amount*0.5)
else:
    total+=amount

if(person3<=12):
    total+=amount-(amount*0.3)
elif(person3>59):
    total+=amount-(amount*0.5)
else:
    total+=amount

if(person4<=12):
    total+=amount-(amount*0.3)
elif(person4>59):
    total+=amount-(amount*0.5)
else:
    total+=amount

if(person5<=12):
    total+=amount-(amount*0.3)
elif(person5>59):
    total+=amount-(amount*0.5)
else:
    total+=amount
print(f'Total payable amount : ',total)