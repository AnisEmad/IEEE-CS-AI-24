def check(num):
    while not num.isdigit():
        num = input("it's not a digit, try again: ")
n = check(input("Enter a number: "))