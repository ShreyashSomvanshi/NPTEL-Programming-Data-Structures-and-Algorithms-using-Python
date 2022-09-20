'''
Question 8
Write a Python function maxdifference(l) that takes a list of pairs of the form (name,score) as argument, where name is a string and score is an integer.
Each pair is to be interpreted as the score of the named player. For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),
('Kohli',66),('Ashwin',90)] represents three scores of 73, 66 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara.
Your function should compute the difference between the maximum and minimum score for each player and return the list of players for whom this difference is maximum.
The list should be sorted in ascending order by the name of the player.

For instance, maxdifference([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Kohli',66),('Ashwin',90)])) 
should return ['Kohli'] because Kohli's difference is 66 (73 - 7), Ashwin's difference is 57 (90 - 33) and Pujara's difference is 0 (122 - 122).

'''

# Instructor's Solution:

def maxdifference(l):
  maximum = {}
  minimum = {}
  for (name,score) in l:
    try:
      maximum[name] = max(maximum[name],score)
      minimum[name] = min(minimum[name],score)
    except KeyError:
      maximum[name] = score
      minimum[name] = score
      
  maxdiff = -1
  maxlist = []

  for name in maximum.keys():
    thisdiff = maximum[name] - minimum[name]
    if thisdiff == maxdiff:
      maxlist.append(name)
    if thisdiff > maxdiff:
      maxdiff = thisdiff
      maxlist = [name]
      
  return(sorted(maxlist))

# import ast

# def tolist(inp):
#   inp = ast.literal_eval(inp)
#   return (inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "maxdifference":
#   arg = tolist(farg)
#   print(maxdifference(arg))

