'''
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will be terminated by a blank line.
The lines are numbered 0,1,2,… Your program should print out the even numbered lines followed by the odd numbered lines.
In other words, first print lines 0,2,4,… then lines 1,3,5,…

'''

'''
Input:                        
Line zero
Line one
Line two
Line three
Line four

Output:
Line zero\n
Line two\n
Line four\n
Line one\n
Line three\n
'''

'''
input:
A few months ago, millions of TV viewers across South Korea were
watching the MBN channel to catch the latest news.  At the top of the
hour, regular news anchor Kim Joo-Ha started to go through the day's
headlines. It was a relatively normal list of stories for late 2020 -
full of Covid-19 and pandemic response updates.  Yet this particular
bulletin was far from normal, as Kim Joo-Ha wasn't actually on the
screen. Instead she had been replaced by a "deepfake" version of
herself - a computer-generated copy that aims to perfectly reflect her
voice, gestures and facial expressions.  Viewers had been informed
beforehand that this was going to happen, and South Korean media
reported a mixed response after people had seen it. While some people
were amazed at how realistic it was, others said they were worried
that the real Kim Joo-Ha might lose her job.

Output:
A few months ago, millions of TV viewers across South Korea were\n
hour, regular news anchor Kim Joo-Ha started to go through the day's\n
full of Covid-19 and pandemic response updates.  Yet this particular\n
screen. Instead she had been replaced by a "deepfake" version of\n
voice, gestures and facial expressions.  Viewers had been informed\n
reported a mixed response after people had seen it. While some people\n
that the real Kim Joo-Ha might lose her job.\n
watching the MBN channel to catch the latest news.  At the top of the\n
headlines. It was a relatively normal list of stories for late 2020 -\n
bulletin was far from normal, as Kim Joo-Ha wasn't actually on the\n
herself - a computer-generated copy that aims to perfectly reflect her\n
beforehand that this was going to happen, and South Korean media\n
were amazed at how realistic it was, others said they were worried\n
'''

# Solution 1:
'''
x=input()
c=0
even = list()
odd = list()
while len(x) > 0:
  if c%2 == 0:
    even.append(x)
    
  else:
    odd.append(x)
  
  x=input()
  c+=1
 
for e in even:
  print(e)
  
for d in odd:
  print(d)

'''





# Instructor's Solution:

inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

for i in range(0,len(inputlines),2):
  print(inputlines[i])
for i in range(1,len(inputlines),2):
  print(inputlines[i])
