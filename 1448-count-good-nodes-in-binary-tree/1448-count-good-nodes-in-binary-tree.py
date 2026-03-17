# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # def dfs (node, maxVal):
        #     if not node:
        #         return 0
        #     res = 0
        #     if node.val >= maxVal:
        #         res += 1
        #     l = dfs(node.left,max(node.val,maxVal))
        #     r = dfs(node.right,max(node.val,maxVal))
        #     return res + l + r
        # return dfs(root,root.val)  

        stack = [(root,root.val)]
        res = 0
        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal:
                res+=1
            if node.left:
                stack.append((node.left,max(maxVal,node.val)))
            if node.right:
                stack.append((node.right,max(maxVal,node.val)))
        return res


                  
        