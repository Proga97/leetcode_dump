"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        qu = deque()
        qu.append([root])
        res = []
        while qu:
            nodes = qu.popleft()
            # print(nodes)
            next_nodes = []
            curr_values = []
            for node in nodes:
                curr_values.append(node.val)
                next_nodes.extend(node.children)
            res.append(curr_values)
            # print(res)
            if next_nodes:
                qu.append(next_nodes)
        return res



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna