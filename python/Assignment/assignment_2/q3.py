#convert distance from feet and inches to meters and cm

feet=float(input("enter distance in feet:"))
inches=float(input("enter distance in inches:"))

# 1 foot = 0.3048 meters, 1 inch = 0.0254 meters

meters=(feet*0.3048)+(inches*0.0254)
centimeters=meters*100

print("distance in meters=",meters)
print("distance in centimeters=",centimeters)