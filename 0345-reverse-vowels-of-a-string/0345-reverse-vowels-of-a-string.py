class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"    
        first, last = 0, len(s) - 1
        array = list(s)
        while first < last:
            while first < last and array[first] not in vowels:
                first += 1
            while first < last and array[last] not in vowels:
                last -= 1

            array[first], array[last] = array[last], array[first]
            first += 1
            last -= 1
        return "".join(array)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna