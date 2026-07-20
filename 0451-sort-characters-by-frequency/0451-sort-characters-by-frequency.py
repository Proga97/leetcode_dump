from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]

        for char, freq in freq_map.items():
            buckets[freq].append(char)
        
        res = ""
        for i in range(len(s), -1, -1):
            if buckets[i]:
                for char in buckets[i]:
                    res += i * char
        return res        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna