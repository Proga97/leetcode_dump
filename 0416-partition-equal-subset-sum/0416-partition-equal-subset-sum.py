class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target / 2
        dp = set()
        dp.add(0)
        for n in nums:
            new_dp = set()
            for r in dp:
                total = n + r
                if total == target:
                    return True
                new_dp.add(total)
                new_dp.add(r)
            dp = new_dp
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna