__author__ = 'matisencale'

from itertools import product
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(string):
    return string == string[::-1]

multiples = ((a,b) for a,b in product(range(100,999), repeat=2) if is_palindrome(str(a*b)))
largest_palindrome_multiples = max(multiples, key=lambda multiple: multiple[0]*multiple[1])

print(largest_palindrome_multiples[0]*largest_palindrome_multiples[1])

#Solution: 906609 = 913 * 993