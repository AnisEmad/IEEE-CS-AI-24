def bayes(a, b, con_b_given_a):
    if not isinstance(a, float) or not isinstance(b, float) or not isinstance(con_b_given_a, float):
        raise TypeError("input must be float numbers")
    res = a * con_b_given_a / b
    return res