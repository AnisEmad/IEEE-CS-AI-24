def common_set(set1={}, set2={}):
    if not isinstance(set1, set) or not isinstance(set2, set):
        print("input must be a set")
        return None
    new_set = set()
    for num in set1:
        if num in set2:
            new_set.add(num)
    return new_set