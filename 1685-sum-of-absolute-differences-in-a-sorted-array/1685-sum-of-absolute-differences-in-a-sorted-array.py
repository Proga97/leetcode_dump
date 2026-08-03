class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        # print(prefix)
        n = len(nums)
        res = []
        for i in range(len(nums)):
            left_sum = prefix[i]
            right_sum = prefix[-1] - prefix[i] - nums[i]

            left_count = i
            right_count = n - i - 1

            left_diff =  (left_count * nums[i]) - left_sum
            right_diff = right_sum - (right_count * nums[i])

            res.append(left_diff + right_diff)
        
        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna