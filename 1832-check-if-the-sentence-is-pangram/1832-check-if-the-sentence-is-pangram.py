class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        # Iterate over each character using a normal for loop
        for i in sentence:            
            seen.add(i)

        return len(seen) == 26

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna