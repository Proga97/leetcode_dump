# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        paths = 0
        def dfs(node,curr_path):
            if not node:
                return 0
            curr_path.append(node.val)
            path_sum = 0
            paths = 0
            for i in range(len(curr_path)-1,-1,-1):
                path_sum += curr_path[i]
                if path_sum == targetSum:
                    paths += 1       

            
            paths += dfs(node.left,curr_path[:])
            paths +=  dfs(node.right,curr_path[:])
            return paths

        return dfs(root,[])
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna