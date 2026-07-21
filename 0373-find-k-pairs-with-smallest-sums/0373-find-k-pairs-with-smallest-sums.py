class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or not k:
            return res        
        heap = []
        
        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(res) < k:
            sum_val, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna