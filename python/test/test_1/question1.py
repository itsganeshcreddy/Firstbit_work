#calculate area and perimeter of rect and cir

length=float(input("enter the length of rect:"))
breadth=float(input("enter the breadth of rect:"))
radius=float(input("enter a radius of circle:"))

#calculate rectangle
area_rect=length*breadth
peri_rect=2*(length+breadth)

#calculate circle
area_cir=3.14*radius*radius
peri_cir=2*3.14*radius

total_area=peri_rect+1/2*peri_cir


print("area of rect=",area_rect)
print("perimeter=",peri_rect)
print("area of circle=",area_cir)
print("perimeter=",peri_cir)

print("total area=",total_area)