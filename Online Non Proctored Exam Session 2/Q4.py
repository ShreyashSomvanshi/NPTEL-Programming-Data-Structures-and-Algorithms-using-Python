'''
Question 4
Recall that the positions in a list of length n are 0,1,…,n-1. We want to write a function mod3pos(l) that returns the elements at all positions in l that are
divisible by 3. In other words, the function should return the list [l[0],l[3],...].
For instance mod3pos([]) == [], mod3pos([7]) == [7], mod3pos([8,11,8,11]) == [8,11] and mod3pos([19,3,44,44,3,19,17,23]) == [19,44,17].
A recursive definition of mod3pos is given below. You have to fill in the missing argument for the recursive call.

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(...)

Open up the code submission box below and fill in the missing argument for the recursive call.
'''

# Instructor's Solution:

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(
       # Complete the recursive call below this line
        [l[0]] + mod3pos(l[3:])
       # Complete the recursive call above this line
    )

# import ast

# def tolist(inp):
#   inp = ast.literal_eval(inp)
#   return(inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "mod3pos":
#   arg = tolist(farg)
#   print(mod3pos(arg))


