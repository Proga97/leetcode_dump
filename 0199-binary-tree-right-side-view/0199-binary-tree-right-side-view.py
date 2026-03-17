# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            lLen = len(q)
            temp = None
            print("ilen",lLen)
            for _ in range(lLen):
                node = q.popleft()
                print(node.val,temp)
                if temp == None:
                    temp = node.val
                    print("temp",temp)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            res.append(temp)
        # print(res)
        return res

        