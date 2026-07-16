# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head or k <= 1:
        #     return head
        
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            last_node_in_set = self.getkThNode(prevGroup,k)
            if not last_node_in_set:
                break
            
            nextGroup = last_node_in_set.next
            curr = prevGroup.next
            prev = nextGroup
            i = 0
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = last_node_in_set
            prevGroup = temp

        return dummy.next


    

    def getkThNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1  
        return curr
            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna