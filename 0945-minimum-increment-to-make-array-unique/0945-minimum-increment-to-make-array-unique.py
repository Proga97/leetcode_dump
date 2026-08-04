class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        freq_map = [0] * (len(nums) + max_val)

        for n in nums:
            freq_map[n] += 1
        
        min_increments = 0
        for i in range(len(freq_map)):
            
            if freq_map[i] <= 1:
                continue
            
            dup = freq_map[i] - 1
            freq_map[i + 1] += dup
            min_increments += dup
            # freq_map[val] = 1 # optional
        
        return min_increments
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna