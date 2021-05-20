# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return None
        
        level_order = [[root]]
        
        while(level_order[-1] != []):
            new_level = []
            for node in level_order[-1]:
                if node.left != None:  
                    new_level.append(node.left)
                if node.right != None:
                    new_level.append(node.right)
            level_order.append(new_level)
            
        return [[node.val for node in depth] for depth in level_order[:-1]]
