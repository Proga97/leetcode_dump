class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        hottest = 0 
        for i in range(len(temperatures)-1, -1, -1):
            curr_temp = temperatures[i]
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            days = 1
            while temperatures[i + days] <= curr_temp:
                days += ans[i + days]
            ans[i] = days
        return ans
        




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna