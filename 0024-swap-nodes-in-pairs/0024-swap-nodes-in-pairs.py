# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head


        start = head.next
        first = head
        second = head.next

        while first and second:
            nex = second.next
            second.next = first
            if nex and nex.next: first.next = nex.next
            else: first.next = nex
            first = nex
            if nex: second = nex.next
            else: second = None
            
            
        
        # print(head,"hi",head.next,":mmmmm",start)
        return start

        

        