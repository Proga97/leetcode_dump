# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        qu = collections.deque()
        qu.append(root)
        res = []
        while qu:
            lLen = len(qu)
            # print(nodes)
            level = []
            for _ in range(lLen):
                n = qu.popleft()
                level.append(n.val)
                if n.left:
                    qu.append(n.left)
                if n.right:
                    qu.append(n.right)
            res.append(level)
        # print(res)
        return res    


        