class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums == None or len(nums) == 0:
            return []
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1,len(nums)):
            res[i] = res[i-1] + nums[i]
        return res