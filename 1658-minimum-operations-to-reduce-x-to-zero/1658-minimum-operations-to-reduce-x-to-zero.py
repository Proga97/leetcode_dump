class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        mini = inf
        left = 0

        for right in range(n):
            # sum([0,..,left) + (right,...,n-1]) = x
            current -= nums[right]
            # if smaller, move `left` to left
            while current < x and left <= right:
                current += nums[left]
                left += 1
            # check if equal
            if current == x:
                mini = min(mini, (n-1-right)+left)

        return mini if mini != inf else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna