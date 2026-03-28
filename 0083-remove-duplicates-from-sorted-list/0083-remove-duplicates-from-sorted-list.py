# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        while curr:
            nex = curr.next
            while nex and curr.val == nex.val:
                # print(curr.val,nex.val)
                curr.next = nex.next
                nex = nex.next
            curr = curr.next
        return head
        