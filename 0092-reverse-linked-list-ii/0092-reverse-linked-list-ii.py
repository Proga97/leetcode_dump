# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
    
        curr, prev = head, None
        
        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        last_node_of_first_part = prev
        last_node_of_sub_list = curr

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev

        last_node_of_sub_list.next = curr
        return head
        


        



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna