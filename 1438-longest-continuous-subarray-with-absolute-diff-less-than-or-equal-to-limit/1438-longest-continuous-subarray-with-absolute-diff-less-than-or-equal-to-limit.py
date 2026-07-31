class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # arr = SortedDict()            
        # left, max_l = 0, 0

        # for r in range(len(nums)):
        #     n = nums[r]
        #     if n in arr:
        #         arr[n] += 1
        #     else:
        #         arr[n] = 1
            
        #     while  arr.items()[-1][0] - arr.items()[0][0] > limit:
        #         arr[nums[left]] -= 1
        #         if arr[nums[left]] == 0:
        #             arr.pop(nums[left])
        #         left += 1
            
        #     max_l = max(max_l, r-left + 1)
        # # print(arr.items()[0], arr.items()[-1])
        # return max_l

        min_q, max_q = deque(), deque()
        left, max_l = 0, 0

        for right in range(len(nums)):
            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            
            max_q.append(nums[right])
            min_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left +=1
            
            max_l = max(max_l, right - left + 1)
        return max_l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna