class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        res = []

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = True
            return True

           

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
                

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna