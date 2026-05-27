class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()

        ## Two pointers
        i = 0
        j = len(s) - 1

        while j > i:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # print(s[i], s[j])
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
        ### comparing ends
        # res = []
        # for a in s:
        #     if a.isalnum():
        #         res.append(a)
        # # print(res)
        # for i in range(len(res)//2):
        #     # print(res[i],res[-i])
        #     if res[i] != res [-i-1]:
        #         return False
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna