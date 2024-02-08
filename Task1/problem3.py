#task 1 probem 3
import math

number = int(input("Enter a number: "))
factorial = math.factorial(number)
print(f"The factorial of {number} is {factorial} (", end="")
for i in range(number, 2, -1):
    print(f"{i} * ", end="")
print("1)")