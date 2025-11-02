#5. Write a program to accept an integer amount from user and tell minimum  
# number of notes needed for representing that amount. (Use looping to optimize  
# the problem)


amount = int(input("Enter the amount: "))

total_notes = 0

print("\nMinimum number of notes required:")


for note in range(1, 8): 
    if note == 1:
        value = 2000
    elif note == 2:
        value = 500
    elif note == 3:
        value = 200
    elif note == 4:
        value = 100
    elif note == 5:
        value = 50
    elif note == 6:
        value = 20
    elif note == 7:
        value = 10
    else:
        pass

    if amount >= value:
        count = amount // value
        amount = amount % value
        total_notes += count
        print(value, ":", count)

print("\nTotal notes needed:", total_notes)
