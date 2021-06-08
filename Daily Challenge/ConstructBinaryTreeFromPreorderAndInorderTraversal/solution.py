# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(preorder == []):
            return None
        
        root = TreeNode(val = preorder[0])
        ind = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:ind+1],inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:],inorder[ind+1:])
            
        return root        
        
