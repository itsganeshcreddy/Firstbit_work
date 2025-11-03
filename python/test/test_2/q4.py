# 4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

choice = input("You want to calculate the painting cost (yes/no): ")

if choice == "yes":
    length = float(input("Enter the length of each wall (in meters): "))
    height = float(input("Enter the height of each wall (in meters): "))
    cost_per_sq_meter = float(input("Enter the cost of painting per square meter: "))

    total_area = 4 * length * height
    total_cost = total_area * cost_per_sq_meter

    print(f"Total wall area: {total_area:.2f} square meters")
    print(f"Total painting cost: {total_cost:.2f}")

elif choice == "no":
    print("Painting cost calculation skipped.")

else:
    print("Invalid input! Please type 'yes' or 'no'.")

