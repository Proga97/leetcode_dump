class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_counter = 0
        for n in nums:
            if n-1 not in nums:
                count = 1
                while n + 1 in nums:
                    count += 1
                    n = n + 1
                max_counter = max(count, max_counter)
        return max_counter


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna