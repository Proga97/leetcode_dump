class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = []
        open_brackets = []

        for i in range(len(s)):
            if s[i] == "(":
                open_brackets.append(i)
            elif s[i] == "*":
                star_count.append(i)
            else:
                if open_brackets: open_brackets.pop()
                elif star_count: star_count.pop()
                else: return False
        
        while open_brackets and star_count and open_brackets[-1] < star_count[-1]:
            open_brackets.pop()
            star_count.pop()
        
        return len(open_brackets) == 0 

        ##### DP 
        dp = {}
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

        # for c in s:
        #     if c == "(":
        #         open_brackets += 1
        #     elif c == ")":
        #         open_brackets -= 1
        #     else:
        #         star_count += 1
        
        # print(open_brackets, star_count)

        # return abs(open_brackets) <= star_count  
 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna