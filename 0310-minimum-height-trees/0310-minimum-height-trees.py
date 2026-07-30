class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        leaves = deque()
        for src, nei in graph.items():
            if len(nei) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nei in graph[leaf]:
                    graph[nei].remove(leaf)
                    if len(graph[nei]) == 1:
                        leaves.append(nei)

        return [0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna