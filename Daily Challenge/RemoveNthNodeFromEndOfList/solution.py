# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None : return None
        start = head
        
        head = None
        tail = start
        n -= 1
        while(n != 0):
            tail = tail.next
            n -= 1
            
        while(tail!=None and tail.next != None):
            tail = tail.next
            if(head == None):
                head = start
            else:
                head = head.next
        
        if(head == None):
            start = start.next
        else:
            head.next = (head.next).next
        
        return start
