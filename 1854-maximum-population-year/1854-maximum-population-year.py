class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101

        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
        
        max_popu = 0
        max_year = 1950
        curr_popu = 0
        for year in range(len(population)):
            curr_popu += population[year]
            if curr_popu > max_popu:
                max_popu = curr_popu
                max_year = 1950 + year
        
        return max_year


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna