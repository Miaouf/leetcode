class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:       
        L = [root]
        while (True):
            val = 0
            new_L = []
            for i in L:
                if(i != None):
                    val += i.val
                    if(i.left != None): new_L.append(i.left)
                    if(i.right != None): new_L.append(i.right)
            
            if(new_L == []):
                return val
            else:
                L=new_L
