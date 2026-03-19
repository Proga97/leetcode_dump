class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # l = 0
        # r = len(nums) - 1
        # k = len(nums) - k 

        # while 0 <= r < len (nums):
        #     pivot = r
        #     p = l
        #     for i in range(l,r):
        #         if nums[i] < nums[pivot]:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p],nums[r] = nums[r],nums[p]
        #     if p == k: return nums[p]
        #     if p < k: l = p + 1
        #     if p > k: r = p - 1

        # def quick_select(l,r):
        #     pivot =  r
        #     p = l
        #     for i in range(l,r):
        #         if nums[i] < nums[pivot]:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p],nums[r] = nums[r],nums[p]
        #     if p == k: return nums[p]
        #     if p < k: quick_select(p + 1,r)
        #     if p > k: quick_select(l, p -1)
        # return quick_select(l,r)

        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap,n)
            else:
                heapq.heappushpop(heap,n)
        return heap[0]

