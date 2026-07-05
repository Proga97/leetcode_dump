# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # total_sum = 0
        def dfs(node, curr):
            if not node:
                return 0
            number = 10 * curr + node.val
            if not node.left and not node.right:
                return number
            return dfs(node.left,number) + dfs(node.right,number)
        # dfs(root,0)
        return dfs(root,0)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna