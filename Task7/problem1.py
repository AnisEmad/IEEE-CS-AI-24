def prob(my_list):
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list of integers")
    for i in my_list:
        if not isinstance(i, int):
            raise TypeError("Input must be numerical.")
    mydict = dict()
    for elm in my_list:
        if elm in mydict:
            mydict[elm] += 1
        else:
            mydict[elm] = 1
    for key, value in mydict.items():
        mydict[key] = value / len(my_list)
    return mydict