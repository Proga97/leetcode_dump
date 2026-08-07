class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(k):
            freq[nums[i]] += 1

        res = []
        res.append(len(freq))

        for i in range(k, len(nums)):
            freq[nums[i-k]] -= 1
            if freq[nums[i-k]] <= 0: del freq[nums[i-k]] 
            freq[nums[i]] += 1
            res.append(len(freq))
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna