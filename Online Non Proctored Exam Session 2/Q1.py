'''
Question 1
Here is an function to return the minimum value in a list. There is an error in this function. Provide an input list for which minbad produces an incorrect output.

def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)
  
'''
#

# Instructor's Solution:

myinput='''
[4,3,2,1]
'''

def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)

# import ast

# try:
#    myarg =  ast.literal_eval(myinput.strip())
# except:
#    print(False)
# else:
#   try:
#      print(minbad(myarg) != min(myarg))
#   except:
#      print(False)
