# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zig = False
        res = []
        qu = deque()
        qu.append([root])
        while qu:
            curr_roots = qu.popleft()
            next_roots = []
            curr_vals = []
            for curr in curr_roots:
                curr_vals.append(curr.val)
                if curr.left:
                    next_roots.append(curr.left)
                if curr.right:
                    next_roots.append(curr.right)
            if zig:
                res.append(curr_vals[::-1])
            else:
                res.append(curr_vals)  
            zig = not zig  
            if next_roots:
                qu.append(next_roots)
            
        return res


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna