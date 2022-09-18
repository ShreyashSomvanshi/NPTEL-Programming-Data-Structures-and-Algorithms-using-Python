'''
Question 5
A positive integer n is a sum of three cubes if n = i^3 + j^3 + k^3 for integers i,j,k such that i ≥ 1, j ≥ 1 and k ≥ 1. For instance, 10 is a sum of three 
cubes because 10 = 1^3 + 1^3 + 2^3, and so is 36 (1^3 + 2^3 + 3^3). On the other hand, 4 and 11 are not sums of three cubes.

Write a Python function sum3cubes(n) that takes a positive integer argument and returns True if the integer is a sum of three cubes, and False otherwise.

'''

# Instructor's Solution:

def cube(n):
    for i in range(1,n+1):
        if n == i**3:
            return(True)
    return(False)

def sum3cubes(n):
    for i in range(1,n-1):
        for j in range (1,n-i):
            k = n - (i+j)
            if cube(i) and cube(j) and cube(k):
                return(True)
    return(False)
# import ast

# def toint(inp):
#   inp = ast.literal_eval(inp)
#   return (inp)

# fncall = input()
# lparen = fncall.find("(")
# rparen = fncall.rfind(")")
# fname = fncall[:lparen]
# farg = fncall[lparen+1:rparen]

# if fname == "sum3cubes":
#   arg = toint(farg)
#   print(sum3cubes(arg))
