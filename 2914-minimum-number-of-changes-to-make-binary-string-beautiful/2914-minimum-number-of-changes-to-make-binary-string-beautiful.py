class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]

        res = 0
        count = 0 

        for c in s:
            if c == curr:
                count += 1
                continue
            
            if count % 2 == 0:
                count = 1
            else:
                count = 0
                res += 1
            
            curr = c
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna