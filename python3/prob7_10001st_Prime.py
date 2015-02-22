__author__ = 'matisencale'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
#is prime for values greater than 2
def is_prime(n):
    if n%2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

#finds nth primes less than n**2
def find_nth_prime(n):
    prime_count = 1
    for i in range(3, n*n):
        if is_prime(i):
            prime_count+=1
        if prime_count==n:
            return i

print(find_nth_prime(10001))

#Solution: 104743