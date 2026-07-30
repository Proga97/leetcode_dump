class UnionFind:
    def __init__(self, edges):
        self.parent = [i for i in range(len(edges) + 1)]
        self.rank = [1] * (len(edges) + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 != p2:
            if self.rank[p2] > self.rank[p1]:
                self.rank[p2] += self.rank[p1]
                self.parent[p1] = p2
            else:
                self.rank[p1] += self.rank[p2]
                self.parent[p2] = p1
            return False
        return True

class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(edges)

        for e1, e2 in edges:
            if uf.union(e1, e2):
                return [e1, e2]
        
        return []


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna