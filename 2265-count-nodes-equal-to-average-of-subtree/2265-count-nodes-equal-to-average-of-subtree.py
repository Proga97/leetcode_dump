# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def postOrder(node):
            nonlocal res
            if not node: return 0, 0
            lsum, lc = postOrder(node.left)
            rsum, rc = postOrder(node.right)

            node_sum = lsum + rsum + node.val           
            node_count = lc + rc + 1
            # print(lsum, rsum, node_count, lc, rc, node.val)
            if (node_sum)// node_count == node.val: res += 1

            return node_sum, node_count 

        postOrder(root)
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna