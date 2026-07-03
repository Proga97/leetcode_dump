# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_even(self, num):
        return num % 2 == 0
    def is_odd(self, num):
        return num % 2 != 0
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        ans = 0
        qu = deque()
        qu.append([root])
        while qu:
            curr_roots = qu.popleft()
            next_roots = []
            if self.is_even(level):
                prev_val = float("-inf")
            else:
                prev_val = float("inf")
            for curr in curr_roots:
                # print("val",level,prev_val,curr.val)
                if self.is_even(level):
                    if self.is_even(curr.val) or curr.val <= prev_val:
                        # print("even",level,curr.val)
                        return False
                elif self.is_odd(level):
                    if self.is_odd(curr.val) or curr.val >= prev_val:
                        # print("odd",level,curr.val)
                        return False
                prev_val = curr.val

                if curr.left:
                    next_roots.append(curr.left)
                if curr.right:
                    next_roots.append(curr.right)
                
            level += 1 
            if next_roots:
                qu.append(next_roots)
            
        return True



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna