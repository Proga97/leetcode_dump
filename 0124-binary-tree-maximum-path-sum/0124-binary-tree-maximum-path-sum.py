# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(node):
            nonlocal max_sum 
            if not node:
                return 0
            
            l_d = max(dfs(node.left),0)
            r_d = max(dfs(node.right),0)

            max_sum = max(max_sum, l_d + r_d + node.val)

            return max(l_d,r_d) + node.val

        dfs(root)

        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna