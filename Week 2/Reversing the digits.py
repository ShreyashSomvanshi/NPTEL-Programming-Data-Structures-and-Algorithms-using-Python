'''
Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

>>> intreverse(783)
387
>>> intreverse(242789)
987242
>>> intreverse(3)
3

'''

# Solution:
def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

