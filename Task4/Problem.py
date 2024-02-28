import math
def get_numbers():
    """ takes list from user """
    data_set = []
    print("Enter the elements of the list, type 'done' to finish: ")
    while True:
        num = input("_: ")
        if num.lower() == 'done':
            break
        try:
            num = int(num)
        except ValueError:
            print("Number must be intger, try again: ")
            continue
        data_set.append(num)
    return data_set

def find_min(numbers):
    """returns minimum number """
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

def find_max(numbers):
    """return maximum number """
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def find_mean(numbers):
    """calculate mean of the list and return it """
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def count_x(numbers, x):
    count = 0
    for number in numbers:
        if number == x:
            count += 1
    return count
def find_mode(numbers):
    """calculate mode of the list and return it """
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    max_count = max(count.values())
    if max_count == 1:
        return None
    modes = [key for key, value in count.items() if value == max_count]
    return modes

def find_median(numbers):
    """ return the median of the list """
    mid = int(len(numbers) / 2)
    sorted_numbers = list(sorted(numbers))
    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[mid] + sorted_numbers[mid - 1]) / 2
    else:
        mid = int(mid)
        median = sorted_numbers[mid]
    return median

def find_range(numbers):
    """return the range of the data set """
    min = find_min(numbers)
    max = find_max(numbers)
    return max - min

def find_variance(numbers):
    mean = find_mean(numbers)
    sum = 0
    for number in numbers:
        sum += (number - mean) ** 2

    return sum / (len(numbers) - 1)

def find_STD(numbers):
    return math.sqrt(find_variance(numbers))

def find_Quariles(numbers):
    numbers = list(sorted(numbers))
    Q2 = int(find_median(numbers))
    if len(numbers) % 2 == 0:
        Q1 = find_median(numbers[:int(len(numbers)/2)])
        Q3 = find_median(numbers[int(len(numbers)/2):])
    else:
        Q1 = find_median(numbers[:int(len(numbers)/2)])
        Q3 = find_median(numbers[int(len(numbers)/2) + 1:])
    Quariles = (Q1, Q2, Q3)
    return Quariles

def find_IQR(numbers):
    qs = find_Quariles(numbers)
    return qs[2] - qs[0]
numbers = get_numbers()
print(numbers)
print(f"Min: {find_min(numbers)}")
print(f"Max: {find_max(numbers)}")
print(f"Mean: {find_mean(numbers)}")
print(f"Mode: {find_mode(numbers)}")
print(f"Median: {find_median(numbers)}")
print(f"Range: {find_range(numbers)}")
print(f"Variance: {find_variance(numbers)}")
print(f"Standard Deviation: {find_STD(numbers)}")
print(f"Quartiles: {find_Quariles(numbers)}")
print(f"Interquartile Range: {find_IQR(numbers)}")