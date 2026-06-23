class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        arr = sorted(pairs, key = lambda x: x[1])
        # print(arr)
        curr_end = float("-inf")
        count = 0
        for n in arr:
            if n[0] > curr_end:
                count += 1
                curr_end = n[1]
        # print(count)
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna