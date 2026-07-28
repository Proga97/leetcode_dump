class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        res = []
        for inWard, out  in prerequisites:
            graph[out].append(inWard)
            inDegree[inWard] += 1
        
        qu = deque()

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                qu.append(i)

        while qu:
            node = qu.popleft()
            res.append(node)

            for n in graph[node]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    qu.append(n)
            
                    

        # print(res)
        return res if len(res) == numCourses else []
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna