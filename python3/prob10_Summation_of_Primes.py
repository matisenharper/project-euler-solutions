__author__ = 'matisencale'

from python3.prob5_Smallest_Multiple import product

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def get_primes_below_value(n):
    pass
#    all_values

#    return prime_lst

#product(prime_lst)
#http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared
                is_prime[i] = False
    for i in range(limit + 1):
        if is_prime[i]: yield i


print(sum(list(iprimes_upto(2000000))))

#Solution: 142913828922