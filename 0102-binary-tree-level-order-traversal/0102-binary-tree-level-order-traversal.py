# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        qu = deque()
        qu.append([root])
        while qu:
            curr_nodes = qu.popleft()
            next_nodes = []
            ans = []
            for curr in curr_nodes:
                ans.append(curr.val)
                if curr.left:
                    next_nodes.append(curr.left)
                if curr.right:
                    next_nodes.append(curr.right)
            res.append(ans)
            if next_nodes:
                qu.append(next_nodes)
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna