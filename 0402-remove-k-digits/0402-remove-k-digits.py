class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
       
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1 
            stack.append(n)

        if k > 0:
            stack = stack[:-k]

        res = "".join(stack)

        return "".join(stack).lstrip("0") or "0"

        # return str(int(res)) if res else "0"  ## remove leading zeros by convrt to int 

        return "".join(stack).lstrip("0") or "0"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna