class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total = 0, 0
        freq_map = defaultdict(int)
        freq_map[0] = 1

        for n in nums:
            total += n
            if total - k in freq_map:
                count += freq_map[total - k]
            freq_map[total] += 1
        
        return count

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna