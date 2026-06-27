class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        # Iterate over each character using a normal for loop
        for i in range(len(sentence)):
            # Convert the current character to lowercase
            currChar = sentence[i].lower()
            
            if currChar.isalpha():
                # Add the character to the set
                seen.add(currChar)

        # Return true if set size is 26 (total number of alphabets)
        return len(seen) == 26

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna