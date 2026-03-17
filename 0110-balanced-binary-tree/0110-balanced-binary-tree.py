# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._depth(root) != -1

    def _depth(self,root) -> int:
        if not root:
            return 0
        
        l = self._depth(root.left)
        if l == -1:
            return -1
        
        r = self._depth(root.right)
        if r == -1:
            return -1
        
        if abs(l-r) > 1:
            return -1
        
        return 1+max(l,r)

        