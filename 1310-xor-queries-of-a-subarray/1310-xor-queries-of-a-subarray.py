class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        res = []

        for l, r in queries:
            res.append(prefix[r+1] ^ prefix[l])
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna