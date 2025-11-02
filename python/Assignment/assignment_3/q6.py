# calculate profit or loss. 

cost_price=float(input("Enter cost price:"))
sale_price=float(input("Enter sale price:"))

profit = sale_price-cost_price
loss = cost_price-sale_price

if(sale_price > cost_price):
    print(f'{profit} rupees Profit.')
elif(cost_price > sale_price):
    print(f'{loss} rupees Loss.')   
else:
    print("No Profit, No Loss.")     