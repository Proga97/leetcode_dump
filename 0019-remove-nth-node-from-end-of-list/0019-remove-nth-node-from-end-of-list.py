# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0,head)
        l, r = d, head
        while n > 0 and r:
            # print("r",r)
            r = r.next
            n -= 1

        while r:
            # print('l,r',l,r)
            l = l.next
            r = r.next
        # print("lll",l)    
        if l.next:
            l.next = l.next.next
        
        # print("lll",l,d)    
        return d.next


        