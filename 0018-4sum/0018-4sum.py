class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        for i in range(0, len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.search_pairs(nums, target, i, j, quadruplets)
        return quadruplets


    def search_pairs(self,arr, target_sum, first, second, quadruplets):
        left = second + 1
        right = len(arr) - 1
        while (left < right):
            quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
            if quad_sum == target_sum:  
                quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])
                left += 1
                right -= 1
                while (left < right and arr[left] == arr[left - 1]):
                    left += 1  
                while (left < right and arr[right] == arr[right + 1]):
                    right -= 1  
            elif quad_sum < target_sum:
                left += 1  
            else:
                right -= 1  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna