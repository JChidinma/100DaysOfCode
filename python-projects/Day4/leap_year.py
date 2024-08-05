# Leap year = (year % 4) == 0, (year%100) != 0 except (year%400) == 0
# else: Not leap year
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
year = int(input("Enter any year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a Leap year")
        else:
            print("Not a leap year")
    else:
        print("This is a Leap year")
else:
    print("Not a leap year")
