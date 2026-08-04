# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val = 0, next = head)
        prev = dummy
        curr = head.next
        while curr:
            val = 0
            while curr and curr.val != 0:
                val += curr.val
                curr = curr.next
            prev.next = ListNode(val = val)
            prev = prev.next
            curr = curr.next
        return dummy.next




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna