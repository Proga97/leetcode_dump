class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 1:
            return False
        preR = collections.defaultdict(list)
        for c, r in  prerequisites:
            preR[c].append(r)
        # print(preR)

        seen = set()
        def dfs(c):
            if len(preR[c]) == 0: return True
            if c in seen: return False 

            seen.add(c)
            for r in preR[c]:
                if not dfs(r): return False
            seen.remove(c)
            preR[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True

        