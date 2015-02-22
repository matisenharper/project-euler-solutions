__author__ = 'matisencale'

'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(n):
    sum_of_sq = 1
    for i in range(1,n+1):
        sum_of_sq+=i*i
    return sum_of_sq

def square_of_sum(n):
    sum_to_square = 0
    for i in range(1,n+1):
        sum_to_square+=i
    return sum_to_square**2

def get_sum_of_square_difference(n):
    return abs(sum_of_squares(n)-square_of_sum(n))

print(get_sum_of_square_difference(100))

#Solution: 25164149