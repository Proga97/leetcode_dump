class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        num_empty = 0
        emptyBottles = 0

        while numBottles > 0:
            drank += numBottles
            emptyBottles += numBottles

            numBottles = emptyBottles//numExchange 
            emptyBottles =  emptyBottles % numExchange

        return drank
            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna