class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = 0
        open_brackets = 0

        dp = {}
        # for c in s:
        #     if c == "(":
        #         open_brackets += 1
        #     elif c == ")":
        #         open_brackets -= 1
        #     else:
        #         star_count += 1
        
        # print(open_brackets, star_count)

        # return abs(open_brackets) <= star_count        

        def dfs(count, index):
            if count < 0: return False
            if index == len(s): return count == 0
            if (count, index)in dp: return dp[(count, index)]

            dp[(count, index)] = False
            if s[index] == "(":
                dp[(count, index)] = dfs(count + 1, index + 1)
            elif s[index] == ")":
                dp[(count, index)] = dfs(count - 1, index + 1)
            else:
                dp[(count, index)] = dfs(count, index + 1) or dfs(count + 1, index + 1) or dfs(count - 1, index + 1)

            
            return dp[(count, index)] 

        return dfs(0,0)   



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna