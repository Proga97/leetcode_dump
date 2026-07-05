# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        qu = deque()
        qu.append((root,1))
        while qu:
            curr,level = qu.popleft()
            if curr.left or curr.right:
                if curr.left:
                    qu.append((curr.left,level+1))
                if curr.right:
                   qu.append((curr.right,level+1))
            else:
                return level 
        return level
        # qu = deque()
        # qu.append([root])
        # level = 0
        # while qu:
        #     curr_nodes = qu.popleft()
        #     level += 1
        #     next_nodes = []
        #     for curr in curr_nodes:
        #         if curr.left or curr.right:
        #             if curr.left:
        #                 next_nodes.append(curr.left)
        #             if curr.right:
        #                 next_nodes.append(curr.right)
        #         else:
        #             return level
        #     qu.append(next_nodes)
        # return level
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna