# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._diameter = 0

        def findDepth(root) -> int:
            if not root:
                return 0

            l = findDepth(root.left)
            r = findDepth(root.right)    
            self._diameter = max(self._diameter, l+r)
            return 1 + max(l,r)
        
        findDepth(root)

        return  self._diameter

    
        