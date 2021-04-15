# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_value = 0
        first_N = None
        prev_N = None
        while((l1 != None or l2 != None) or add_value!=0):
            if(l1 != None):
                add_value += l1.val
                l1 = l1.next
            if(l2 != None):
                add_value += l2.val
                l2 = l2.next
                
            new_N = ListNode(val=add_value%10)
            add_value = add_value//10
            if(prev_N!=None):
                prev_N.next = new_N
            else:
                first_N = new_N
            
            prev_N = new_N

        return first_N
