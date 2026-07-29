class Solution:
    def alienOrder(self, words: List[str]) -> str:
        inDegree = {}
        graph = defaultdict(set)
        prevWord = words[0]

        for word in words:
            for c in word:
                inDegree[c] = 0

        for word in words[1:]:
            for c1, c2 in zip(prevWord, word):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        inDegree[c2] += 1 
                    break
            else:
                if len(word) < len(prevWord):
                    return ""
            prevWord = word

        qu = deque()
        for c in inDegree:
            if inDegree[c] == 0:
                qu.append(c)

        # print(graph)
        # print(inDegree)
        # print(qu)
        res = ""
        while qu:
            char = qu.popleft()
            res += char

            for child in graph[char]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    qu.append(child)

        if len(res) < len(inDegree):
            return ""
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna