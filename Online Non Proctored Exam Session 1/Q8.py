'''
Question 8
Write a Python function aboveaverage(l) that takes a list of pairs of the form (name,score) as argument, where name
is a string and score is an integer. Each pair is to be interpreted as the score of the named player. For instance,
an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)] represents two scores of 73
and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara. Your function should compute the
list of players whose individual average score is greater than or equal to the overall average score. For an individual
player, the average score is the total across all scores for that player divided by number of entries for that player.
The overall average score is the total across all scores for all the players divided by the total number of entries
across all players. The list should be sorted in ascending order by the name of the player.

For instance, aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) should
return ['Pujara'] because the overall average score is 65 (325 divided by 5), Kohli's average is 40, (80 divided by 2),
Ashwin's average is 61.5 (123 divided by 2) and Pujara's average is 122 (122 divided by 1)
'''

'''
input: aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',142),('Ashwin',90)])
output: ['Pujara']\n

input: aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)])
output: ['Ashwin', 'Kohli']\n
'''


# Instructor's Solution:
def aboveaverage(l):
  aggregate = {}
  innings = {}
  totalscore = 0
  totalinnings = 0
  for (name,score) in l:
    totalscore += score
    totalinnings += 1
    try:
      aggregate[name] += score
      innings[name] += 1
    except KeyError:
      aggregate[name] = score
      innings[name] = 1

  overallaverage = totalscore/totalinnings

  aboveaverage = []
    
  for name in aggregate.keys():
    average = aggregate[name]/innings[name]
    if average >= overallaverage: 
      aboveaverage.append(name)
      
  return(sorted(aboveaverage))

# import ast

# def tolist(inp):
#   inp = ast.literal_eval(inp)
#   return (inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "aboveaverage":
#   arg = tolist(farg)
#   print(aboveaverage(arg))



# Solution 1:
'''
def aboveaverage(l):
  d={}
  for i in l:
    name,score = i
    if name in d:
      tot_score, num = d[name]
      d[name] = (tot_score+score,num+1)
    else:
      d[name] = (score,1)
  max = -1
  for k in d:
    tot_score, num=d[k]
    ave = tot_score/num
    if(max < ave):
      max = ave
  l=[]
  for k in d:
    tot_score, num = d[k]
    ave = tot_score/num
    if(max == ave):
      l.append(k)
          
  l.sort()
  return l
'''
