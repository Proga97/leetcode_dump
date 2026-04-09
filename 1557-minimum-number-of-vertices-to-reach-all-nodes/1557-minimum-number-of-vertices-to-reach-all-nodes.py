class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seen = set()
        res = set()
        for fro, to in edges:
            seen.add(to)
        for fro, to in edges:
            if fro not in seen:
                res.add(fro)
        # print(res)
        return list(res)

        