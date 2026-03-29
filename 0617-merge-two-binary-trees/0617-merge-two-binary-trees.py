# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        if not root1 or not root2:
            return root1 or root2
        
        # root = TreeNode(root1.val + root2.val)

        def trans (root1,root2):
            if not root1:
                return root2
            if not root2:
                return root1
            
            node = TreeNode(root1.val+root2.val)
            node.left = trans(root1.left,root2.left)
            node.right = trans(root1.right,root2.right)

            return node
        root = trans(root1,root2)
        # print(root)
        return root
        