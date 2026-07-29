class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        inDegree = {}
        graph = defaultdict(list)

        for n in nums:
            inDegree[n] = 0

        for seq in sequences:
            for i in range(len(seq) - 1):
                parent, child = seq[i], seq[i + 1]
                graph[parent].append(child)
                inDegree[child] += 1 

        qu = deque()
        for c in inDegree:
            if inDegree[c] == 0:
                qu.append(c)
        
        # print(graph, inDegree,qu)
        res = []
        while qu:
            if len(qu) > 1:
                return False

            n = qu.popleft()
            if nums[len(res)] != n:
                return False
            res.append(n)

            for child in graph[n]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    qu.append(child)

        return len(res) == len(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna