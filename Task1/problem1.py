#Task 1 problem 1

largest = float("-inf")
smallest = float("inf")
while True:
    number = int(input("Enter any number or -1 to terminate: "))
    if number == -1:
        break
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print(largest, smallest)
    