'''
Question 6
Write a Python function uncommon(l1,l2) that takes two lists sorted in ascending order as arguments and returns the list of all elements that appear in exactly
one of the two lists. The list returned should be in ascending order. All such elements should be listed only once, even if they appear multiple times in l1 or l2.

Thus, uncommon([2,2,4],[1,3,3,4,5]) should return [1,2,3,5] while uncommon([1,2,3],[1,1,2,3,3]) should return [].

'''

#  Solution:

def uncommon(l1,l2):
  s1=set(l1)
  s2=set(l2)
  union = s1 | s2
  intersection = s1 & s2
  ans = list(union - intersection)
  ans.sort()
  return ans

# import ast

# def topairoflists(inp):
#     inp = "["+inp+"]"
#     inp = ast.literal_eval(inp)
#     return (inp[0],inp[1])

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "uncommon":
#    (arg1,arg2) = topairoflists(farg)
#    print(uncommon(arg1,arg2))
