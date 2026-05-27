class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = Counter(nums)
        # print(counter_map)
        # heap = []
        # for key, value in counter_map.items():
        #     heapq.heappush(heap,(value,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # # print(heap)
        # res = []
        # for (value, key) in heap:
        #     res.append(key)
        # # print(res)
        # return res

        #Bucket Sort
        buckets = [[] for _ in range(len(nums) + 1)]
        # print(buckets)
        for key, value in counter_map.items():
            buckets[value].append(key)
        # print(buckets)
        res = []
        for i in range(len(buckets) - 1 ,0,-1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna