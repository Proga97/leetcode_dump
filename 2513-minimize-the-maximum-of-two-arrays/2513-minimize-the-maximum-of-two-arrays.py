import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low = uniqueCnt1 + uniqueCnt2
        high = uniqueCnt1 * divisor1 * uniqueCnt2 * divisor2
        LCM = math.lcm(divisor1, divisor2)
        while low <= high:
            mid = (low + high) // 2
            common_count = mid // LCM

            if (mid - common_count) >= uniqueCnt1 + uniqueCnt2 and (mid - (mid // divisor1)) >= uniqueCnt1 and (mid - mid // divisor2) >= uniqueCnt2:
                high = mid - 1
            else:
                low = mid + 1
        return low



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna