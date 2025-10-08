#convert days into year,weeks and days

days=int(input("enter the days="))

#calculate year,weeks,days
years=days//365
remaining_days=days%365
weeks=remaining_days//7
days_left=remaining_days%7

print("year=",years)
print("week=",weeks)
print("day=",days_left)