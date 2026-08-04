# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helperNode = head.next
        sumNode = helperNode

        while sumNode:
            accumulatedSum = 0
            # Accumulate sum of nodes between zeros
            while sumNode.val != 0:
                accumulatedSum += sumNode.val
                sumNode = sumNode.next

            # Assign the accumulated sum to the current node's value
            helperNode.val = accumulatedSum
            # Move sumNode to the first non-zero value of the next segment
            sumNode = sumNode.next
            # Move helperNode also to this node
            helperNode.next = sumNode
            helperNode = helperNode.next

        return head.next        
        dummy = ListNode(val = 0, next = head)
        prev = dummy
        curr = head.next
        while curr:
            val = 0
            while curr.val != 0:
                val += curr.val
                curr = curr.next
            prev.next = ListNode(val = val)
            prev = prev.next
            curr = curr.next
        return dummy.next




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna