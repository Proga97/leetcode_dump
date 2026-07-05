# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, sum, nodes):
            if not root:
                return 
            sum -= root.val
            nodes.append(root.val)
            if not root.left and not root.right and sum == 0:
                res.append(nodes[:])
            dfs(root.left,sum,nodes[:])
            dfs(root.right,sum,nodes[:])
        dfs(root,targetSum,[])
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna