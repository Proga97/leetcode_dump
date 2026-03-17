class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ma = collections.defaultdict(int)
        for n in nums:
            ma[n] += 1
        # heap 
        # heap = []
        # for key,v in ma.items():
        #     heapq.heappush(heap,(v,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # # print(heap)
        # arr = []
        # for n in heap:
        #     arr.append(n[1])
        # # print(arr)
        # return arr

        # bucket
        arr = [[] for _ in range(len(nums)+1)]
        for key,v in ma.items():
            arr[v].append(key)
        # print(arr)
        res = []
        for i in range(len(arr)-1,0,-1):
            for z in arr[i]:
                res.append(z)
                if len(res) == k: 
                    # print(res)
                    return res


        
        