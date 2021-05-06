# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 
# Basic implementation
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
       
        def BST_middle(head, tail):
            if(head == tail):
                return None
            root = head
            end = head
            while(end != tail and end.next != tail):
                root = root.next
                end = end.next.next

            return TreeNode(root.val,BST_middle(head, root) ,BST_middle(root.next, tail))
        
        return BST_middle(head,None)
"""
# With list preprocessing
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        val = []
        while(head != None):
            val.append(head.val)
            head = head.next
            
        def build_BST(i, j):
            if(i >= j):
                return None
            middle = (i+j)//2
            return TreeNode(val[middle],build_BST(i,middle),build_BST(middle+1,j))
        
        return build_BST(0,len(val))
        
