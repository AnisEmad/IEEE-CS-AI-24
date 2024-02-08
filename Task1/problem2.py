#Task 1 problem 2

day = int(input("Day: "))
month = int(input("Month:"))
year = int(input("Year: "))

day += 1
if month in [1, 3, 5, 7, 8, 10, 12] and day == 32:
    day = 1
    month += 1
elif month in [4, 6, 9, 11] and day == 31:
    day = 1
    month += 1
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and day == 30:
    day = 1
    month += 1
elif day == 29:
    day = 1
    month += 1
if month == 13:
    month = 1
    year += 1
print(f"Day: {day} Month: {month} Year: {year}")
