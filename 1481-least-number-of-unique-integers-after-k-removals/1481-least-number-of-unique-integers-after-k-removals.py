class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        buckets = [0] * (len(arr) + 1)

        for val, count in freq_map.items():
            buckets[count] += 1

        remaining_unique_elements = len(freq_map)

        for i in range(1, len(arr) + 1):
            remove_num_unique = min(k // i, buckets[i])
            k -= (i * remove_num_unique)

            remaining_unique_elements -= remove_num_unique

            if k < i:
                return remaining_unique_elements


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna