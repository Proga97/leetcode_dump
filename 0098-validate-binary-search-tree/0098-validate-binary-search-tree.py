# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def depth(root,lower,upper):
            if not root: return 0

            if not (lower < root.val < upper):
                return -1

            # print(root.val,"val")
            # if not (root.right and lower < root.right.val < upper) : 
            #     print("right",)
            #     return -1
            # if not (root.left and lower < root.left.val < upper): 
            #     return -1

            l =  depth(root.left,lower,root.val)
            if l == -1: return -1

            r =  depth(root.right,root.val,upper)
            if r == -1: return -1

            return 1 + (max(l,r))
        
        return depth(root,float('-inf'),float('inf')) != -1
            