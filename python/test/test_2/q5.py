# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

shoping = input("You are shopping(yes or no) : ")

if(shoping == "yes"):
    p1 = int(input("Enter the p1 price : "))
    p2 = int(input("Enter the p2 price : "))
    p3 = int(input("Enter the p3 price : "))
    p4 = int(input("Enter the p4 price : "))
    p5 = int(input("Enter the p5 price : "))

    c = p1 + p2 + p3 + p4 + p5
    print(c)
    price = 0.18 * c
    total_bill = price + c
    print(total_bill)
else: 
    print("Thank You.") 