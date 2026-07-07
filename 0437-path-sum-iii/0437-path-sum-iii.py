# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        def dfs(node, curr_sum):
            nonlocal paths
            if not node:
                return 0
        
            curr_sum += node.val  
            paths += prefix_map[curr_sum - targetSum]    

            prefix_map[curr_sum] += 1

            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)

            prefix_map[curr_sum] -= 1

        dfs(root,0)

        return paths
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna