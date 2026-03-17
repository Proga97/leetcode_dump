# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l1, l2 = head, head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        curr = l1.next
        prev = None 
        l1.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr 
            curr = next  
        
        first = head
        second = prev
        while second:
            t1, t2 = first.next,second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        
        
        
        
        