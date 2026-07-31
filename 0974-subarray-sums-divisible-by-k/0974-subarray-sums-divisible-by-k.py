class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_freq = defaultdict(int)
        rem_freq[0] = 1
        prefix = 0
        count = 0

        for n in nums:
            prefix += n

            rem = prefix % k
            if rem in rem_freq:
                count += rem_freq[rem]

            rem_freq[rem] += 1
        
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna