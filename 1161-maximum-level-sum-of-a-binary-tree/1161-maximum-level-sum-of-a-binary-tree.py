# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        level = 0
        ans = 0
        qu = deque()
        qu.append([root])
        while qu:
            curr_roots = qu.popleft()
            level += 1
            next_roots = []
            curr_sum = 0
            for curr in curr_roots:
                curr_sum += curr.val
                if curr.left:
                    next_roots.append(curr.left)
                if curr.right:
                    next_roots.append(curr.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level       
            if next_roots:
                qu.append(next_roots)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna