'''
Question 3
The median of three numbers x,y,z is the second number in the sequence when the three numbers are sorted in ascending or descending order.
Here is a function to compute the median of three input integers. You have to fill in the missing lines.

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  # Your code below this line


  # Your code above this line
  return(mymedian)
  
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.
'''

# Instructor's Solution:

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  # Your code below this line

  if x >= y and x <= z:
    mymedian = x
  if y <= x and y >= z:
    mymedian = y
  if y >= x and y <= z:
    mymedian = y
  if z <= x and z >= y:
    mymedian = z
  if z >= x and z <= y:
    mymedian = z
  # Your code above this line
  return(mymedian)
 
  
  
  
# import ast

# def totripleint(inp):
#   inp = "[" + inp + "]"
#   inp = ast.literal_eval(inp)
#   return(inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "median3":
#   arglist = totripleint(farg)
#   print(median3(arglist[0],arglist[1],arglist[2]))
