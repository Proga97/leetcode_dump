class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [0] * len(nums), [0] * len(nums)
        for i in range(1,len(nums)):
            leftSum[i] = leftSum[i-1] + nums[i - 1]
            rightSum[-i - 1] = rightSum[-i] + nums[-i]
        print(leftSum,rightSum)
        return [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]

        