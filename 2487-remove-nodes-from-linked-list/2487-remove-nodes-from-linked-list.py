# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        # curr = head
        # stack = []
        # while curr:
        #     while stack and stack[-1] < curr.val:
        #         stack.pop()
        #     stack.append(curr.val)
        #     curr = curr.next
        # dummy = ListNode(0)
        # curr = dummy
        # for val in stack:
        #     curr.next = ListNode(val)
        #     curr = curr.next
        # return dummy.next

        # with no new creation of linked list
        curr = head
        stack = []
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            if stack:
                stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        
        return stack[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna