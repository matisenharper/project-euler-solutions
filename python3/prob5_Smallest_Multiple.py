__author__ = 'matisencale'

from collections import Counter

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
#returns list of prime factors for n
def get_prime_factors(n):
    prime_factors=[]
    divisor = 2
    while n > 1:
        while n % divisor ==0:
            prime_factors.append(divisor)
            n /= divisor
        divisor = divisor + 1
    return prime_factors

#n must be greater than 2

def product(list):
    p = 1
    for i in list:
        p*=i
    return p

def get_smallest_multiple(n):
    combined = []
    for i in range(2,n+1):
        combined = Counter(combined)|Counter(get_prime_factors(i))
    rv = product(list(combined.elements()))
    return rv

print(get_smallest_multiple(20))

#Solution: 232792560