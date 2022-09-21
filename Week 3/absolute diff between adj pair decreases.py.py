'''
Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements 
strictly decreases.

Here are some examples of how your function should work.
 >>> contracting([9,2,7,3,1])
  True

  >>> contracting([-2,3,7,2,-1]) 
  False

  >>> contracting([10,7,4,1])
  False

'''
# Solution:
def contracting(l):
  for i in range(0,len(l)-3):
    if (abs(l[i+2]-l[i+1])<abs(l[i+1]-l[i])):
      continue
    else:
      return False
  return True
