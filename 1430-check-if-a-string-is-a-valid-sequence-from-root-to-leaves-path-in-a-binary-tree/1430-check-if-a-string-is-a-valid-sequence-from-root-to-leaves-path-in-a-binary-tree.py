# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if not root:
            return False
        res = ""
        for s in arr:
            res += str(s)
        def dfs(node, curr, res):
            if not node:
                return False
            curr = curr + str(node.val)
            if not node.left and not node.right:
                if curr == res:
                    return True
                return False
            return dfs(node.left,curr,res) or dfs(node.right,curr,res)
        return dfs(root,"",res)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna