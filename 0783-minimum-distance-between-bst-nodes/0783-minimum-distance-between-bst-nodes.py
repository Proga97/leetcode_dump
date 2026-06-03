# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.diff = float('inf')
    def trans(self,root):
        if not root: 
            return 0
        self.trans(root.left)

        # self.nodes.append(root.val)
        if self.prev:
            self.diff = min(self.diff, abs(root.val - self.prev.val))
        self.prev = root
        self.trans(root.right)
        

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.trans(root)
        # print(self.nodes)
        # diff = float('inf')
        # for n in range(1,len(self.nodes)):
            # diff = min(diff, abs(self.nodes[n-1] - self.nodes[n]))
            # print(diff)
        return self.diff

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna