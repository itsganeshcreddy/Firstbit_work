# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

pi = 3.1416
r = 20
l = 50
b = 40
cost = 35
times = 5

choice = input("You want to calculate the fencing cost? (yes/no): ")

if choice == "yes":
    # Calculate lengths
    rect_length = (2 * (l + b) - b)    
    circ_length = pi * r              

    total_length = (rect_length + circ_length) * times

    rect_cost = rect_length * times * cost
    circ_cost = circ_length * times * cost

    total_cost = rect_cost + circ_cost

    print("Rectangular part cost = Rs",rect_cost)
    print("Circular part cost = Rs",circ_cost)
    print("Total fencing cost = Rs",total_cost)

else:
    print("Calculation stop...")

