'''
Question 2
Here is an implementation of quicksort, which splits the input list according the pivot value, sorts each part and arranges the sorted parts with the 
pivot in between to give the final sorted sequence. There is a small error in the implementation. Provide an input list for which this version of quicksort
produces an incorrect output.

def quicksortbad(l):
  if len(l) < 2:
    return(l)
  else:
    pivot = l[0]
    smaller = [l[j] for j in range(1,len(l)) if l[j] < pivot]
    bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
    rearrange = quicksortbad(smaller) + [pivot] + quicksortbad(bigger)
    return(rearrange)

Open up the code submission box below and write your test case where you would normally paste your code. Your input should be a list of numbers.
'''

# Instructor's Solution:

myinput='''
[1,1,2]
'''

def quicksortbad(l):
  if len(l) < 2:
    return(l)
  else:
    pivot = l[0]
    smaller = [l[j] for j in range(1,len(l)) if l[j] < pivot]
    bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
    rearrange = quicksortbad(smaller) + [pivot] + quicksortbad(bigger)
    return(rearrange)
    
def quicksortgood(l):
  if len(l) < 2:
    return(l)
  else:
    pivot = l[0]
    smaller = [l[j] for j in range(1,len(l)) if l[j] <= pivot]
    bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
    rearrange = quicksortgood(smaller) + [pivot] + quicksortgood(bigger)
    return(rearrange)
    
import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(quicksortbad(myarg) != quicksortgood(myarg))
  except:
     print(False)


