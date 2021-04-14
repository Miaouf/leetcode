# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = None
        less = None
        greater_head = None
        greater = None
        while(head != None):
            if(head.val < x):
                if(less == None):
                    less_head = head
                    less= head
                else:
                    less.next = head
                    less = head
            else:
                if(greater == None):
                    greater_head = head
                    greater= head
                else:
                    greater.next = head
                    greater = head
            head = head.next
        
        if(less != None):
            less.next = greater_head
        else:
            less_head = greater_head
            
        if(greater != None):
            greater.next = None

        return less_head
