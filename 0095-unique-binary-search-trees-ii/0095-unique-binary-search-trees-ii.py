# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            
            res = []
            for root in range(left, right + 1):
                leftTrees = generate(left, root-1)
                rightTrees = generate(root+1 , right)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        res.append(TreeNode(root, left= leftTree, right = rightTree))
            return res
        
        return generate(1, n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna