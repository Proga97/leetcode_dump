class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        count = 0
        i = 0
        previous_last = -1

        while i < len(s):
            r = i
            l = r - k + 1
            if l > previous_last and check(l, r):
                # print("1", s[l:r+1])
                count += 1
                previous_last = r
                i = r + 1
                continue

            l = r - k
            if l > previous_last and check(l, r):
                # print("2", s[l:r+1])
                count += 1
                previous_last = r 
                i = r + 1
                continue
            
            i += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna