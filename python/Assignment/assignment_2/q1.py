#convert time in hh,min and sec into seconds

hours=int(input("enter hours:"))
minutes=int(input("enter minutes:"))
seconds=int(input("enter seconds:"))

total_sec=hours*3600+minutes*60+seconds

print("total time in seconds=",total_sec)