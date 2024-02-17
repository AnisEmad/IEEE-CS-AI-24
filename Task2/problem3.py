def check_int(n):
    while not n.isdigit():
        n = input("number of runners is not an int: ")
    n = int(n)
    while n < 2:
        n = input("number of runners must be at least 2")
        n = check_int(n)
    return n
def check(n):
    while not n.isdigit():
        n = input("number must be integer: ")
    return int(n)
if __name__ == '__main__':
    n = check_int(input("Enter number of runners: "))
    print("Enter the runners: ")
    arr = []
    for i in range(n):
        tmp = check(input())
        arr.append(tmp)
    mx = max(arr)
    for i in reversed(sorted(arr)):
        if i != mx:
            print(f"Answer: {i}")
            break