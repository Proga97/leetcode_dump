class Solution:
    def minInsertions(self, s: str) -> int:
        open_count = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                open_count += 1
                i += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    res += 1
                if i < len(s) - 1 and s [i + 1] == ")":
                    i += 2
                else: 
                    res += 1
                    i += 1
                    
        res += open_count * 2
        return res 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna