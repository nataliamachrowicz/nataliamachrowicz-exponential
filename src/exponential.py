
def power(a: int, n: int):
    return a**n

def power_zero(a: int):
    return a**0

def power_one(a: int):
    if a == 0:
        raise ValueError('Cannot power zero!')
    return a**1

def add_two_powers(a: int, n: int, m: int):
    return (a**n) * (a**m)

def minus_power(a: int,n: int):
    return a**(-n)