'''
Question 1
Here is an function to return the maximum value in a list. There is an error in this function. Provide an input list for which maxbad produces an incorrect output.

def maxbad(l):
  mymax = l[-1]
  for i in range(-1,-len(l),-1):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)
'''

#Ans : [20,11,12,13]

## Instructor's Code:
myinput='''
[4,3,2,1]
'''

def maxbad(l):
  mymax = l[-1]
  for i in range(-1,-len(l),-1):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)
  return(mymax)

import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(maxbad(myarg) != max(myarg))
  except:
     print(False)




