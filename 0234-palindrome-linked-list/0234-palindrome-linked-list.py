# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        curr = head
        # print(prev,"hi",curr)
        
        while curr and prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True



        