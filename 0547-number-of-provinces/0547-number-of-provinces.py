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
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # seen = [False] * len(isConnected)
        # count = 0
        # stack = []

        # for i in range(len(isConnected)):
        #     if not seen[i]:
        #         stack.append(i)
        #         count += 1  
        #         while stack:
        #             n = stack.pop()
        #             for j in range(len(isConnected[n])):
        #                 if isConnected[n][j] and not seen[j]:
        #                     stack.append(j)
        #                     seen[j] = True

                            
        # return count
        n = len(isConnected)
        uf = UnionFind(n)
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= uf.union(i,j)
        # print(uf.parent,res)
        return res









        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna