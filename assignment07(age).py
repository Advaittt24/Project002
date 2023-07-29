year1 = int(input("Enter Your Birth Year = "))
month1 = int(input("Enter Your Birth Month = "))
day1 = int(input("Enter Your Birth Day = "))

year2 = int(input("Enter Current Year = "))
month2 = int(input("Enter Current Month = "))
day2 = int(input("Enter Current Day = "))

year = year2 - year1
month = month2 - month1
day = day2 - day1

print("Your Birth Year is = ",year1)
print("Your Birth Month is = ",month1)
print("Your Birth Day is = ",day1)

print("Current Year is = ",year2)
print("Current Month is = ",month2)
print("Current Day is = ",day2)

print("Your Current Age is = ",year)
print("Your Current Month is = ",month)
print("Your Current Day is = ",day)