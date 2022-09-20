'''
Question 6
Write a Python function disjointlist(l1,l2) that takes two lists as arguments and returns True if the two lists are disjoint, otherwise returns False.

Two lists are said to be disjoint if there is no element that common to both the lists.
For instance, [2,2,3,4,5] and [6,8,8,1] are disjoint, while [1,2,3,4] and [2,2] are not.
'''

# Instructor's Solution:

def disjointlist(l1,l2):
  s1 = set(l1)
  s2 = set(l2)
  return(s1 & s2 == set())
# import ast

# def topairoflists(inp):
#   inp = "["+inp+"]"
#   inp = ast.literal_eval(inp)
#   return (inp[0],inp[1])

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "disjointlist":
#   (arg1,arg2) = topairoflists(farg)
#   print(disjointlist(arg1,arg2))
