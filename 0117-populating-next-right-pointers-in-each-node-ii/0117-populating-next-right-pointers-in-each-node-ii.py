"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        qu = deque()
        qu.append([root])
        while qu:
            curr_nodes = qu.popleft()
            next_level = []
            for i in range(len(curr_nodes)):
                curr = curr_nodes[i]
                if i < len(curr_nodes) - 1:
                    curr.next = curr_nodes[i+1]
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            if next_level:
                qu.append(next_level)
        return root
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna