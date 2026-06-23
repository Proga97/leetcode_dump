class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for n in num:
            freq[int(n)] += 1
        res = []
        middle = -1
        for i in range(len(freq) - 1,-1,-1):
            if i != 0 or len(res) > 0:
                n = freq[i]
                while n > 1:
                    res.append(str(i))
                    n -= 2
                if n ==1 and  middle == -1:
                    middle = i
        sec_half = res[::-1]
        if middle != -1: res.append(str(middle))
        res.extend(sec_half)
        return "".join(res) or "0"








        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna