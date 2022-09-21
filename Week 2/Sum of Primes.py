'''
Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

>>> sumprimes([3,3,1,13])
19
>>> sumprimes([2,4,6,9,11])
13
>>> sumprimes([-3,1,6])
0
'''

# Solution: 
def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
  return(factors(n) == [1,n])


def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)

