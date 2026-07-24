class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[len(nums) - 1] = True

        def dfs(index):
            if index >= len(nums) - 1:
                return 0
            if nums[index] == 0:
                return math.inf
            if dp[index] != -1:
                return dp[index]
            
            possible_jumps = min(index + nums[index], len(nums) - 1)
            jumps = math.inf
            for i in range(possible_jumps, index, -1):
                jumps = min(jumps, dfs(i) + 1)
                
            dp[index] = jumps
            return dp[index]

        
        return dfs(0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna