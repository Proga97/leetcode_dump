class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations= {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
        }

        def backtrack(left, right):
            res = []

            for i in range(left,right):
                curr = expression[i]
                if curr in operations:
                    nums1 = backtrack(left,i)
                    nums2 = backtrack(i+1,right)

                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[curr](n1,n2))
            if not res:
                res.append(int(expression[left:right]))
            return res
        
        return backtrack(0, len(expression))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna