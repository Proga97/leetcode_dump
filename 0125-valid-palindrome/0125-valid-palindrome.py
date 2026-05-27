class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        res = []
        for a in s:
            if a.isalnum():
                res.append(a)
        # print(res)
        for i in range(len(res)//2):
            # print(res[i],res[-i])
            if res[i] != res [-i-1]:
                return False
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna