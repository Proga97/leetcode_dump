class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for n in nums2:
            while stack and stack[-1] < n:
                hashmap[stack.pop()] = n
            stack.append(n)
        
        res = []
        for n in nums1:
            x = hashmap.get(n, -1)
            res.append(x)
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna