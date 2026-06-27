class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortestDistance = len(wordsDict) 
        position1, position2 = -1, -1 
        for i, word in enumerate(wordsDict):
            if word == word1: 
                position1 = i
            elif word == word2: 
                position2 = i
            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))

        return shortestDistance

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna