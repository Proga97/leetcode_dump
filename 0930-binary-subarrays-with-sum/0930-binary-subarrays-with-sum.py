class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cum_sum, count = 0, 0
        cum_sum_map = defaultdict(int)

        for i in range(len(nums)):
            cum_sum += nums[i]

            if cum_sum == goal:
                count +=1
            
            if cum_sum - goal in cum_sum_map:
                count += cum_sum_map[cum_sum - goal]
            
            cum_sum_map[cum_sum] += 1
        
        return count

             


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna