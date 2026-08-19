class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        l = 0
        freq = defaultdict(int)
        for r in range(len(s2)):
            freq[s2[r]] += 1
            while l <= r and (s2[r] not in s1_map or freq[s2[r]] > s1_map[s2[r]]): 
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0: del freq[s2[l]]
                l += 1
            # print(freq, l , r)
            if freq == s1_map: return True

        return False

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna