class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        curr = set()
        length = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1

            curr.add(s[r])
            if len(curr) > length:
                length = len(curr)
        return length



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna