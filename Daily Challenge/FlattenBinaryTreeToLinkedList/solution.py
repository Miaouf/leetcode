# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root == None):
            return None
        
        start = root
        end = root.right
        root.right = self.flatten(root.left)
        root.left = None
        while(root.right != None):
            root = root.right
            
        root.right = self.flatten(end)
        return start
