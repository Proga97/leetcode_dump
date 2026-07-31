class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr = SortedDict()            
        left, max_l = 0, 0

        for r in range(len(nums)):
            n = nums[r]
            if n in arr:
                arr[n] += 1
            else:
                arr[n] = 1
            
            while  arr.items()[-1][0] - arr.items()[0][0] > limit:
                arr[nums[left]] -= 1
                if arr[nums[left]] == 0:
                    arr.pop(nums[left])
                left += 1
            
            max_l = max(max_l, r-left + 1)
        # print(arr.items()[0], arr.items()[-1])
        return max_l

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna