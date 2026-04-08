class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        seen = [0] * n
        safe = []
        def dfs(node):
            # print(node)
            if seen[node] == 1:
                # print("seen")
                return True
            if seen[node] == -1:
                # print("seen false",seen[node])
                return False
            seen[node] = -1
            if len(graph[node]) == 0:
                # print("00",graph[node],node)
                seen[node] = 1
                return True
            for i in graph[node]:
                if not dfs(i):
                    return False
            seen[node] = 1
            return True

        for i in range(len(graph)):
            if dfs(i):
                safe.append(i)
        # print(safe)
        return safe
                

        