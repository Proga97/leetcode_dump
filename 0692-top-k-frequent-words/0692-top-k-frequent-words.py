class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        # print(freq)
        heap = []
        for string, count in freq.items():
            heappush(heap, (-count, string))
        
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna