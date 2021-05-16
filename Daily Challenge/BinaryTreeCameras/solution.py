# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 2 monitored, 1 has camera
        
        def childrenMonitored(node):
            return not (node.left != None and node.left.val == 0) and not (node.right != None and node.right.val == 0)
                
        def isLeaf(node):
            return (node.left == None and node.right == None)
        
        def updateChildren(node):
            if(node.left != None and node.left.val == 0):
                node.left.val = 2
                
            if(node.right != None and node.right.val == 0):
                node.right.val = 2
        
        
        stack = []
        ans = 0
        lastVisited = None
        if(root.left == None and root.right == None):
            return 1
        
        while(stack != [] or root != None):
            if(root != None):
                stack.append(root)
                root = root.left
                
            else:
                peek = stack[-1]
                if(peek.right != None and peek.right != lastVisited):
                    root = peek.right
                else:    
                    lastVisited = stack.pop()
                    if((not isLeaf(lastVisited) and not childrenMonitored(lastVisited)) or (lastVisited.val == 0 and stack == [])):
                        ans += 1
                        lastVisited.val = 1
                        updateChildren(lastVisited)
                        if(stack != []):
                            stack[-1].val = 2 #update parent  
        return ans
