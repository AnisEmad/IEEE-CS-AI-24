def test_type(year):
    while True:
        try:
            year = int(year)
            break
        except:
            year = input("Please enter an intger number: ")
    return year
def test_signal(year):
    if year <= 0:
        year = input("Please enter a poistive number: ")
    return test_type(year)
def check(year):
    year = test_type(year)
    year = test_signal(year)
    return year
def is_leap(year):
    leap = False
    year = check(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    return leap

year = input("Enter a year: ")
print(is_leap(year))