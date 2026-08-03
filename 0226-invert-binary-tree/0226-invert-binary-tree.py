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
        self.root = None
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.root = root
        num_threads = os.cpu_count()
        # print(num_threads)
        return self.invert_tree_multi(root, num_threads)

    def invert_tree_multi(self, node, num_threads):
        if not node:
            return 
        node.left, node.right = node.right, node.left
        if num_threads > 0:
            def invert_right_tree():
                nonlocal node, num_threads
                self.invert_tree_multi(node.right, num_threads//2)
            
            t1 = threading.Thread(target = invert_right_tree)
            t1.start()

            self.invert_tree_multi(node.left, num_threads//2)

            t1.join()
        else:
            self.invert_tree_multi(node.right, num_threads) 
            self.invert_tree_multi(node.left, num_threads)

        return self.root
     


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna