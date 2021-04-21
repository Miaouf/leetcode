"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

""" 
# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if(root == None):
            return []
        else:
            L = [root.val]
            for i in root.children :
                L += self.preorder(i)
            return L
"""
# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if(root == None):
            return []
        else:
            val = []
            L = [root]
            while(L != []):
                root = L[0]
                val.append(root.val)
                L = root.children + L[1:]
            return val
