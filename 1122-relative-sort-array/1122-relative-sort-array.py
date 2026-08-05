class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        count = defaultdict(int)
        for n in arr1:
            count[n] += 1
        
        for i in arr2:
            for _ in range(count[i]):
                res.append(i)
            del count[i]
        
        count = sorted(count.items())
        rem = []
        for key, co in count:
            for _ in range(co):
                rem.append(key)
        
        res.extend(rem)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna