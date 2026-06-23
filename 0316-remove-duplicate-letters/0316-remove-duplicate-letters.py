class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i in range(len(s)):
            last_occur[s[i]] = i
        # print(last_occur)
        stack = []
        seen = set()
        for i in range(len(s)):
            c = s[i]
            if c not in seen:
                while stack and c < stack[-1] and i < last_occur[stack[-1]]:
                    # print(stack,c)
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna