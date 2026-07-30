class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, n):
        res = n
        while res!= self.parent[res]:
            self.parent[res] =  self.parent[self.parent[res]]
            res = self.parent[res]
        return res
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1
        
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(len(graph))

        for n1 in range(len(graph)):
            if not graph[n1]:
                continue
            first_nei = graph[n1][0]
            p1 = uf.find(n1)

            for n2 in graph[n1]:
                if p1 == uf.find(n2):
                    return False
                uf.union(first_nei, n2)

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna