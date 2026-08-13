class Solution:
    def reverse(self, x: int) -> int:
        signed_max = "2147483647" 
        s = str(x)
        s = list(s)
        l = 0
        if s[0] == "-":
            l = 1
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        s = "".join(s)        
        digits = s[1:] if s[0] == "-" else s
        digits = digits.lstrip('0')
        if len(digits) > len(signed_max):
                # print("000herer")
                return 0
        elif len(digits) == len(signed_max):        
            if digits > signed_max:
                # print("herer",digits,signed_max)
                return 0
        
        return int(s)
        




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna