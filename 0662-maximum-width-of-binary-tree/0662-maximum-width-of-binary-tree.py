# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return []
        max_width = 0
        qu = deque()
        qu.append([(root,0)])
        while qu:
            curr_roots = qu.popleft()
            # print(curr_roots)
            # max_width = max(max_width,len(curr_roots))
            first = curr_roots[0][1]
            last = curr_roots[-1][1]
            next_roots = []
            for (curr, index) in curr_roots:
                if curr.left:
                    next_roots.append((curr.left,2 * index))
                if curr.right:
                    next_roots.append((curr.right, 2 * index + 1))
            max_width = max(max_width,last - first + 1)
            if next_roots:
                qu.append(next_roots)
            
        return max_width




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna