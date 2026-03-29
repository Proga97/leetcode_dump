# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        arr = [0]
        # ress = 0
        def inOrder(node):
            if not node:
                return
            
            if node.val < low:
                inOrder(node.right)
            elif node.val > high:
                inOrder(node.left)
            else:
                # arr.append(node.val)
                arr[0] += node.val
                # ress = ress + node.val 
                inOrder(node.left)
                inOrder(node.right)
        inOrder(root)
        # print(arr)
        # print(arr)
        return arr[0]

        