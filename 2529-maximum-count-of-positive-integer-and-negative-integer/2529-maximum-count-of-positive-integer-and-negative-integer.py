class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        max_negatives, max_positives = len(nums) , len(nums) 

        while start <= end:
            mid = (start + end)//2
            if nums[mid] < 0:
                start = mid + 1   
            else:
                end = mid - 1
                max_negatives = mid 

    
        start, end = 0, len(nums ) - 1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                max_positives = mid

        max_positives = len(nums)-max_positives
        # print(mid,max_positives , max_negatives)
        return max(max_positives, max_negatives)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna