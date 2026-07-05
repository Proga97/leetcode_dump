# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, curr):
            if not node:
                return ""
            number = curr + str(node.val)
            if not node.left and not node.right:
                res.append(number)
            dfs(node.left,number)
            dfs(node.right,number)
        dfs(root,"")
        return sum(int(num) for num in res)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna