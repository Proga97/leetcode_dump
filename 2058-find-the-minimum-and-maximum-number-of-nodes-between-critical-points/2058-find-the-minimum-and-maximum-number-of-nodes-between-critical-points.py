# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]


        index = 1
        prev, curr, next = head, head.next, head.next.next
        c_points = []
        while next:
            if curr.val < prev.val and curr.val < next.val:
                c_points.append(index)
            elif curr.val > prev.val and curr.val > next.val:
                c_points.append(index)
            
            prev, curr, next = curr, next, next.next
            index += 1
        
        if len(c_points) < 2:
            return [-1, -1]

        min_d = float("inf")
        max_d = c_points[-1] - c_points[0]
        # print(c_points)

        for i in range(len(c_points) - 1):
            min_d = min(c_points[i+1] - c_points[i], min_d)
        
        return [min_d, max_d]

        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna