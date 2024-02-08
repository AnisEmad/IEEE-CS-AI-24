#task 1 problem 6

num = int(input("Enter a number: "))
sum = 0
add = 2
numbers = list()
while add <= num:
    sum += add
    numbers.append(add)
    add += 2
print(f"The sum of even numbers from 1 to {num} is {sum} (", end="")
for i in range(0, len(numbers)):
    print(numbers[i], end="")
    if i != len(numbers) - 1:
        print(" + ",end="")
    else:
        print(")")