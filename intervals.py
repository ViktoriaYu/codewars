'''
A format for expressing an ordered list of integers is to use
a comma separated list of either
    individual integers
    or a range of integers denoted by the starting integer
        separated from the end integer in the range by a dash, '-'.
        The range includes all integers in the interval includingboth endpoints.
        It is not considered a range unless it spans at least 3 numbers.
        For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing
order and returns a correctly formatted string in the range format. 
'''

def solution(args):
    k = 1
    i = 1
    res = str(args[0])
    while i < len(args):
        while i < len(args) and args[i] == args[i-1] + 1:
            k += 1
            i += 1
            
        if k > 2:
            res += '-' + str(args[i-1])
        elif k == 2:
            res += ',' + str(args[i-1])
            
        if i < len(args):
            res += ',' + str(args[i])
        i += 1
        k = 1
        
    return res


#a = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
#b = solution(a)
#print(b)
