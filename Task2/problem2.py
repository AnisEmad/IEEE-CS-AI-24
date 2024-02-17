def test_name(name):
    while not name.isalpha():
        name = input("Name must be string, enter the name again: ")
    return name
def test_score(score):
    try:
        score = float(score)
        return score
    except Exception:
        score = input("Score must be float, enter it again: ")
    return test_score(score)
def test_number(n):
    try:
        m = int(n)
        while m < 2:
            m = test_number(input("Students must 2 at least: "))
        return m
    except Exception:
        m = input("number of students must be integer: ")
    return test_number(m)
def bubble_sort(students):
    n = len(students)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        if not swapped:
            break
        
if __name__ == '__main__':
    students = []
    for _ in range(test_number(input("Enter the number of students: "))):
        name = test_name(input("Enter name: "))
        score = test_score(input("Enter Score: "))
        students.append([name, score])
    bubble_sort(students)
    ans = []
    n = students[0][1]
    for i in range(1, len(students)):
        if students[i][1] != n:
            n = students[i][1]
            break
    for i in students:
        if i[1] == n:
            ans.append(i[0])
    for name in sorted(ans):
        print(name)
