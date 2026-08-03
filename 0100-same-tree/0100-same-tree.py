import os
import threading
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isSame = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        num_threads = os.cpu_count()
        # print(num_threads)
        return self.isSameMultiThread(p, q, num_threads)

    def isSameMultiThread(self, p, q, num_threads):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        if num_threads > 0:
            def check_right_tree():
                nonlocal p, q, num_threads
                self.isSame &= self.isSameMultiThread(p.right, q.right, num_threads//2)
            
            t1 = threading.Thread(target = check_right_tree)
            t1.start()

            self.isSame &= self.isSameMultiThread(p.left, q.left, num_threads//2)

            t1.join()
        
        else:
            self.isSame &= self.isSameMultiThread(p.left, q.left, num_threads) and self.isSameMultiThread(p.right, q.right, num_threads)

        return self.isSame
     
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna