'''
Background
Starting with the closed interval [0,1], the Cantor ternary set is constructed
by iteratively applying the operation "remove the middle thirds",
by which we mean removing the open interval ((2a+b)/3,(a+2b)/3)
from each remaining closed interval [a,b]. If Cn denotes the result
after n iterations, then C0=[0,1], C1=[0,1/3]∪[2/3,1] and
C2=[0,1/9]∪[2/9,1/3]∪[2/3,7/9]∪[8/9,1].
To be precise, the Cantor ternary set, C, is the result after infinitely
many iterations. In other words, C is the intersection of all the sets Cn.

Task
Given a rational number (i.e. a fraction) q and a non-negative integer n,
decide whether q is in Cn. More precisely, you must write a function whose
parameters are two positive integers num and den and an integer n.
Your function must return True or False depending on whether
the rational number num / den is in Cn or not.
'''

import sys
sys.setrecursionlimit(9999)

def cantor(num, den, n):
    if n == 0:
        return [0, 1]
    else:
        c = cantor(num, den, n-1)
        eps = 1e-11
        if c == False:
            return False
        if num/den < (2*c[0] + c[1]) / 3 or abs(num/den - (2*c[0] + c[1]) / 3) < eps:
            return [c[0], (2*c[0] + c[1]) / 3]
        elif num/den > (c[0] + 2*c[1]) / 3 or abs(num/den - (c[0] + 2*c[1]) / 3) < eps:
            return [(c[0] + 2*c[1]) / 3, c[1]]
        else:
            return False

def is_in_cantor(num, den, n, eps=1e-10):
    c = cantor(num, den, n)
    if c == False:
        return False
    else:
        f = num/den
        return (f > c[0] or abs(f - c[0]) < eps) and (f <= c[1] or abs(f - c[1]) < eps)
