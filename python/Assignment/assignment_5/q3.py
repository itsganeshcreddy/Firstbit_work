#3. Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition : 
#           a. Children below 12 = 30% discount 
#           b. Senior citizen (above 59) = 50% discount 
#           c. Others need to pay full.

num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amt = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        result = ticket_cost * 0.70
        print(f"Passenger {i} (Child): ₹{result:.2f}")
    elif age > 59:
        result = ticket_cost * 0.50
        print(f"Passenger {i} (Senior Citizen): ₹{result:.2f}")
    else:
        result = ticket_cost
        print(f"Passenger {i} (Normal): ₹{result:.2f}")

    total_amt += result

print(f"\nTotal amount to be paid for all passengers: ₹{total_amt}")
