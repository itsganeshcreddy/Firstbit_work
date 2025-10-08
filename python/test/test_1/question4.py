#calculate cost of paint the building wall(both interior and exterior),you need area of one wall
#total walls to paint= 8-1 = 7

#area in sq.m

area=float(input("enter the area of one wall :"))
int_cost=float(input("enter the interior wall cost: "))
ext_cost=float(input("enter the exterior wall cost: "))

total_walls=7         # 8 common wall -1 shared wall
int_walls=5
ext_walls=2

total_int_area=int_walls*area
total_ext_area=ext_walls*area

#calculate total cost

total_cost=(total_int_area*int_cost)+(total_ext_area*ext_cost)

print("total interior painting cost=",total_int_area*int_cost)
print("total exterior painting cost=",total_ext_area*ext_cost)
print("total painting cost=",total_cost)


