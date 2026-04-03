class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = []
        visited = set()
        stack.append(source)
        while stack:
            x = stack.pop()
            if x == destination: return True
            if x not in visited:
                visited.add(x)
                for n in graph[x]:
                    if x == destination: return True
                    if n not in visited: stack.append(n)
        return False
        