class Solution:
    def sortVowels(self, s: str) -> str:
        arr = list(s)
        vowels_map = {'a','e','i','o','u','A','E',"I","O","U"}
        vowels_counter = defaultdict(int)
        for i in arr:
            if i in vowels_map:
                vowels_counter[i] += 1
        vowels_sorted = 'AEIOUaeiou'
        index = 0
        res = []
        for c in s:
            if c not in vowels_map:
                res.append(c)
            else:
                while vowels_counter[vowels_sorted[index]] <= 0:
                    index += 1
                # if index < len(vowels_map):
                res.append(vowels_sorted[index])
                vowels_counter[vowels_sorted[index]] -= 1
        return "".join(res)

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna