class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        req = len(t)
        l = 0 
        formed = 0
        res = (float("inf"), "")
        freq = defaultdict(int)
        for r in range(len(s)):
            if s[r] in t:
                freq[s[r]] += 1
                if  freq[s[r]] == t[s[r]]: 
                    formed += 1
            
            while l <= r and formed == req:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, s[l: r+1])
                if s[l] in freq:
                    freq[s[l]] -= 1
                    if  freq[s[l]] < t[s[l]]: formed -= 1

                l += 1
        
        return res[1]

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna