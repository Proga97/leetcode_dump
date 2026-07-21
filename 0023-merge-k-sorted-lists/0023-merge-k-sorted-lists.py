# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        heap = []
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            curr.next = ListNode(heappop(heap)) 
            curr = curr.next
        # print(heap)
        
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna