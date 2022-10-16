'''
Given an n x n array, return the array elements
arranged from outermost elementsto the middle element, traveling clockwise.
'''

def snail(snail_map):
    if len(snail_map[0]) == 0:
        return []
    n = len(snail_map)
    res = []
    x = 0
    i = 0
    j = -1
    il = n
    jl = n
    ir = 0
    jr = -1
    while x < n*n:
        while j < jl-1 and i == ir:
            x += 1
            j += 1
            res.append(snail_map[i][j])     
        jl -= 1
        
        while i < il-1 and j == jl:
            x += 1
            i += 1
            res.append(snail_map[i][j])
        il -= 1
        
        while j > jr+1 and i == il:
            x += 1
            j -= 1
            res.append(snail_map[i][j])
        jr += 1
        
        while i > ir+1 and j == jr:
            x += 1
            i -= 1
            res.append(snail_map[i][j])
        ir += 1

    return res
