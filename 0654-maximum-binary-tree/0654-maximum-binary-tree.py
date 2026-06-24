# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(l,r):
            if l == r:
                return None
            
            max_i = l
            for i in range(l,r):
                if nums[i] > nums[max_i]:
                    max_i = i
            root = TreeNode(nums[max_i])
            root.left = construct(l,max_i)
            root.right = construct(max_i+1,r)
            return root
        
        return construct(0,len(nums))


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna