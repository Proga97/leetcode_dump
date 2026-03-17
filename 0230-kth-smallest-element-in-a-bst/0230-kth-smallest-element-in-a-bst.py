# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        #recurssive dfs
        # arr = []

        # def inorder(root):
        #     if root is None:
        #         return
        #     if len(arr) < k:
        #         inorder(root.left)    
        #         arr.append(root.val)             
        #         inorder(root.right) 

        # inorder(root)
        # print(arr)               
        # if len(arr) > k: return arr[k-1]
        # else: return arr[-1]
        
        #itterative dfs
        # n = 0 
        # val = root.val
        # curr = root
        # stack = []
        # arr = []
        # while curr or stack:
        #     while curr:  
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     arr.append(curr.val)
        #     curr = curr.right
        # print(arr)
        # return arr[k-1]        
    
        # efficient ittertive dfs
        n = 0 
        curr = root
        stack = []
        while curr or stack:
            while curr:  
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
       
        