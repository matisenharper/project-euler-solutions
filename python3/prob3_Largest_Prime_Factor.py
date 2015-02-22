'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

print(max(get_prime_factors(600851475143)))

#Solution: 6857