'''
Question 2
Here is a function stablesortbad that takes a list of pairs of integers as input and sorts them by the second coordinate in each pair.
A stable sort preserves the order of pairs that have an equal second coordinate. This is not a stable sort. Provide an input for which stablesortbad
produces an output that is not stably sorted. Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].

def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
  
  
Open up the code submission box below and write your test case where you would normally paste your code.
Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].

'''

# Instructor's Solution:

myinput = '''
[(2,3),(5,4),(3,4),(0,1)]
'''

def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
def stablesortgood(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] > l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
# import ast

# try:
#    myarg =  ast.literal_eval(myinput.strip())
# except:
#    print(False)
# else:
#   try:
#      print(stablesortbad(myarg[:]) != stablesortgood(myarg[:]))
#   except:
#      print(False)
