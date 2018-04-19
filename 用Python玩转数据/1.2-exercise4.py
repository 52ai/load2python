# coding:utf-8
from math import sqrt,log


def is_prime_number(num):
    """Judge a number is a prime or not"""

    threshold = int(sqrt(num))
    for i in range(2, threshold):
        if num%i == 0:
            return False
    else:
        return True


def is_monisen_number(num):
    """Judge a number is a monisen or not"""

    if is_prime_number(log(num+1,2)) and is_prime_number(num):
        return True
    return False


def get_monisen_number(n):
    """Get monisen number"""
    if n!=int(n) or n < 1:
        return []
    x = 3
    result= [3]

    while True:
        if is_prime_number(x) and is_prime_number(2**x - 1):
            result.append(2**x -1)
        if len(result) == n:
            return result
        x += 2


print is_prime_number(31)
print is_monisen_number(31)

print get_monisen_number(5)