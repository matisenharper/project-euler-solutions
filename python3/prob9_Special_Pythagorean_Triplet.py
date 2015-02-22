__author__ = 'matisencale'

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagorean_triple(summation):
    for a in range(1, summation):
        for b in range(a+1, summation-a):
            c=summation-a-b # a+b+c =1000
            if a**2+b**2==c**2: 
                return a*b*c

print(pythagorean_triple(1000))

#Solution: 31875000