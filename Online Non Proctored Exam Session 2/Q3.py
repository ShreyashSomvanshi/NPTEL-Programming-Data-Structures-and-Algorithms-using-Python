'''
Question 3
Here is a function to compute the third largest value in a list of distinct integers. All the integers are guaranteed to be positive. You have to fill in the
missing lines. You can assume that there are at least three numbers in the list.

def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  # Your code below this line


  # Your code above this line
  return(mythirdmax)
  
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.
'''

# Instructor's Solution:

def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  # Your code below this line

    if l[i] > mymax:
      (mymax,mysecondmax,mythirdmax) = (l[i],mymax,mysecondmax)
    elif l[i] > mysecondmax:
      (mysecondmax,mythirdmax) = (l[i],mysecondmax)
    elif l[i] > mythirdmax:
      mythirdmax = l[i]

  # Your code above this line
  return(mythirdmax)


# import ast

# def tolist(inp):
#   inp = ast.literal_eval(inp)
#   return(inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "thirdmax":
#   arg = tolist(farg)
#   print(thirdmax(arg))
