class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know = {}
        for key, value in knowledge:
            know[key] = value
        
        # print(know)

        l = -1
        r = 0
        res = []
        for r  in range(len(s)):
            # print(s[r])
            if s[r] == "(":
                # print("here", r , l) 
                l = r
            elif s[r] == ")":
                # print("split", s[l+1:r])
                # print("s", s, res)
                # print(know[s[l+1:r]])
                res.append(know.get(s[l+1:r], "?"))
                l = -1
            elif l < 0:
                res.append(s[r])
        # print(res)
        return "".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna