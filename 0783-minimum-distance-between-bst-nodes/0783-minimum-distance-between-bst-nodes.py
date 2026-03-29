# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        if not root.right and not root.left:
            return

        arr = []

        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)
        inOrder(root)
        print(arr)
        minD = float("inf")
        for i in range(1,len(arr)):
            minD = min(minD,arr[i] - arr[i-1]) 
        return minD
            


        