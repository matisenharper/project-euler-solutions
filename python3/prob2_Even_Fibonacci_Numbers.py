
import fibonacci

'''
Each new term in the Fibonacci sequence is generated by adding the previous two\
 terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed f\
our million, find the sum of the even-valued terms.
'''

fiblist=fibonacci.fib2(4000000)
sum = 0

for i in fiblist:
    if(i%2 == 0):
        sum += i

print(sum)

#Solution:4613732
