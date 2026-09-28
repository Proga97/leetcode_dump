class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        freq = defaultdict(int)
        res =[]
        for n in nums:
            freq[n] += 1

        keys = sorted(freq.keys())
        # print(keys)

        while len(freq) > 0:
            for k in keys:
                if freq[k] > 0:
                    res.append(k)
                    freq[k] -= 1
                if freq[k] == 0: del freq[k]

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna