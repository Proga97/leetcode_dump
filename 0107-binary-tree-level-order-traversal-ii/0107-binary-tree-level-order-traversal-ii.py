# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        qu = deque()
        qu.append([root])
        res = []
        while qu:
            curr_roots = qu.popleft()
            res_values = []
            next_roots = []
            for curr_root in curr_roots:
                res_values.append(curr_root.val)
                if curr_root.left:
                    next_roots.append(curr_root.left)
                if curr_root.right:
                    next_roots.append(curr_root.right)
            if next_roots:
                # print(next_roots)
                qu.append(next_roots)
            if res_values:
                # print(res_values)
                res.append(res_values)
        # print(res)
        return res[::-1]
                


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna