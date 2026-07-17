class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.append(0) # to count all the remainining elemetns left in stack once it reaches end
        stack = []
        res = 0
        for i in range(len(arr)):

            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                smallest_before = stack[-1] if stack else -1
                left_sets = index - smallest_before
                right_sets = i - index
                res = res + (arr[index] * left_sets * right_sets) % MOD

            stack.append(i)
        return res % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna