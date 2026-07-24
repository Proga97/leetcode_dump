class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [-1] * len(nums)

        # def dfs(index):
        #     if index >= len(nums) - 1:
        #         # print("reached",index)
        #         return True if index == len(nums) - 1 else False
        #     if dp[index] != -1:
        #         return dp[index]

        #     possible_jumps = min(index + nums[index], len(nums) - 1)
        #     # print(index, possible_jumps)
        #     for i in range(possible_jumps, index, -1):
        #         if dfs(i):
        #             dp[i] = True
        #             return dp[i]

        #     dp[index] = False
        #     return dp[index]
        
        # return dfs(0)
        
        # greedy approach
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna