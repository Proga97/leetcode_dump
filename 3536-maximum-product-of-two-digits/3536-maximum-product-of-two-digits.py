class Solution:
    def maxProduct(self, n: int) -> int:
        n1 = 0
        n2 = 0 

        n = str(n)
        for i in n:
            i = int(i)
            if i >= n1:
                # print(i)
                n2 = n1
                n1 = i
            elif i > n2:
                n2 = i
        # print(n1, n2)
        return n1 * n2


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna