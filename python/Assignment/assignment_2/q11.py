#number of notes find for given amount

amount=int(input("enter the amount:"))

n2000=amount//2000
amount=amount%2000

n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount=amount%100

n50=amount//50
amount=amount%50

n20=amount//20
amount=amount%20

n10=amount//10
amount=amount%10

total_notes=n2000+n500+n200+n100+n50+n20+n10

print("minumum number of notes =",total_notes)
print("note 2000",n2000)
print("note 500",n500)
print("note 200",n200)
print("note 100",n100)
print("note 50",n50)
print("note 20",n20)
print("note 10",n10)


