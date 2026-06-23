class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        req = 0
        for n in s:
            if n == "(":
                count += 1
            else:
                if count > 0: count -= 1
                else: req += 1
        # print(count)
        return count + req

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna