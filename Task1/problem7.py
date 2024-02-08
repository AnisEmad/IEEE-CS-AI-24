#task 1 problem 7

def prime_factors(n):
    factors = list()
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

num = int(input("Enter a positive integer: "))
    
while num <= 0:
    num = int(input("Please enter a positive integer: "))
factors = prime_factors(num)
print("Prime factors:", ', '.join(map(str, set(factors))))
