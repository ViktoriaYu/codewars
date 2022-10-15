'''
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

Your task is to return the list with elements from tree sorted by levels,
which means the root element goes first, then root children (from left to right)
are second and third, and so on.

Return empty list if root is None.
'''

def depth(node): 
    left_t = 0 
    right_t = 0 
    if node: 
        left_t = depth(node.left) 
        right_t = depth(node.right) 
        return max(left_t, right_t) + 1  
    return 0 
 
    
def by_level(node, level, res = []): 
    if node: 
        if level == 0: 
            res.append(node.value) 
        else: 
            by_level(node.left, level - 1, res) 
            by_level(node.right, level - 1, res) 
    return res
 
    
def tree_by_levels(node): 
    n = depth(node) 
    res = [] 
    for level in range(n+1): 
        by_level(node, level, res) 
    return res
