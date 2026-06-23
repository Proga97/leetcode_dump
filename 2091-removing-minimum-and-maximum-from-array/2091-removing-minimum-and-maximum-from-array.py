class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = -1
        min_val = float("inf")
        max_index = -1
        max_val = float("-inf")
        for i in range(len(nums)):
            n = nums[i]
            if n > max_val:
                max_val = n
                max_index = i
            if n < min_val:
                min_val = n
                min_index = i
        # print(min_val,min_index,max_val, max_index)
        if min_index == max_index:
            return min_index + 1
        remove_front = max(min_index,max_index) + 1
        front_back = min(min_index,max_index) + len(nums) - max(min_index,max_index) + 1
        remove_back = len(nums) - min(min_index,max_index)
        return min(remove_front,front_back,remove_back)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna