def prob(a, b):
    if not isinstance(a, list):
        raise TypeError("Input must be a list of integers")
    for i in a:
        if not isinstance(i, int):
            raise TypeError("Input must be numerical.")
    if not isinstance(b, list):
        raise TypeError("Input must be a list of integers")
    for i in b:
        if not isinstance(i, int):
            raise TypeError("Input must be numerical.")
    inter = 0
    event_a = 0
    for i in range(len(a)):
        if a[i] == 1:
            event_a += 1
        if a[i] == 1 and b[i] == 1:
            inter += 1
    inter = float(inter) / float(len(a))
    event_a = float(event_a) / float(len(a))
    res = float(inter / event_a)
    return res

event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]
print(prob(event_a,event_b))