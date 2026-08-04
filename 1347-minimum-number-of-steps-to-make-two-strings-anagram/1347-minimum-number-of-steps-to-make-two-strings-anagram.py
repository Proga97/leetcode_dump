class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_t = defaultdict(int)

        for ch in t:
            count_t[ch] += 1
        
        for ch in s:
            count_t[ch] -= 1
        
        changes = 0
        for count in count_t.values():
            if count > 0:
                changes += count
        
        return changes 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna