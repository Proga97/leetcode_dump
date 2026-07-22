# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if not l1 or not l2:
        #     return l1 or l2
        
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        curr1 = l1
        curr2 = l2
        while curr1 or curr2 or carry != 0:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2

        return dummy.next
        

            
        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna