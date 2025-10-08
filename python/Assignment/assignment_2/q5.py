#selling  price of books based on cost,price,discount

cost_price=float(input("enter cost price of book:"))
discount=float(input("enter the discount percentage:"))

selling_price=cost_price-(cost_price*discount/100)

print("selling price=",selling_price)