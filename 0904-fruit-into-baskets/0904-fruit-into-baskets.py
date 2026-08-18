class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            freq[fruits[r]] += 1
            while len(freq) > 2:
                # print(freq)
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0: del freq[fruits[l]]
                l += 1
            res = max(res, r - l + 1)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna