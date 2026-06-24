class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def majCheck(low,high):
            if low == high:
                return nums[low]
            
            mid = low + (high - low)// 2
            left_majority = majCheck(low, mid)
            right_majority = majCheck(mid +1, high)

            if left_majority == right_majority:
                return left_majority

            l_count = nums[low:high + 1].count(left_majority)      
            r_count = nums[low:high + 1].count(right_majority) 

            return left_majority if l_count > r_count else right_majority
        
        return majCheck(0,len(nums)-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna