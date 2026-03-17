class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums = set(nums)
       
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                next = n + 1
                l = 1
                while next in nums:
                    l += 1
                    next +=1
                longest = max(longest,l)    
        return longest
        
   
      