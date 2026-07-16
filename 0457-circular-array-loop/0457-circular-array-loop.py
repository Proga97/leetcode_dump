class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            slow = i
            fast = i
            is_forward = nums[i] > 0

            while True:
                slow = self.nextIndex(nums, slow, is_forward)
                fast = self.nextIndex(nums, fast, is_forward)
                if fast != -1:
                    fast = self.nextIndex(nums, fast, is_forward)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            
            if slow != -1 and slow == fast:
                return True

        return False

    def nextIndex(self, arr, curr, is_forward):
            direction = arr[curr] >= 0
            if direction != is_forward:
                return -1
            
            next_index = (curr + arr[curr]) % len(arr)

            if next_index == curr:
                return -1
            
            return next_index



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna