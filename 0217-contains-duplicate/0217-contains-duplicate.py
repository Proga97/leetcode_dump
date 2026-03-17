class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        x = set()
        for n in nums:
            if n in x:
                return True
            x.add(n)
        return False
