# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        qu = deque()
        qu.append([root])
        while qu:
            curr_roots = qu.popleft()
            curr_max = float("-inf")
            next_roots = []
            for curr in curr_roots:
                if curr.val > curr_max:
                    curr_max = curr.val
                if curr.left:
                    next_roots.append(curr.left)
                if curr.right:
                    next_roots.append(curr.right)
            if next_roots:
                qu.append(next_roots)
            res.append(curr_max)
        # print(res)
        return res
            
            
                


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna