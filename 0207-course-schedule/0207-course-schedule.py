class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for out, inWard in prerequisites:
            graph[out].append(inWard)
        seen = set()
        for i in range(numCourses):
            if not self.dfs(graph, i, seen):
                return False
        return True
    
    def dfs(self, graph, node, seen):
        if not graph[node]: return True
        if node in seen: return False

        seen.add(node)
        for n in graph[node]:
            if not self.dfs(graph, n, seen): return False
        seen.remove(node)

        graph[node] = []
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna