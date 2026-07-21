class Solution:
    def reorganizeString(self, s: str) -> str:
        max_count, letter = 0, ""
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
            if freq_map[char] > max_count:
                max_count = freq_map[char]
                letter = char
            if max_count > (len(s) + 1) // 2:
                return ""
        
        arr = [""] * len(s)
        index = 0

        while freq_map[letter] > 0:
            arr[index] = letter
            index += 2
            freq_map[letter] -= 1
        
        for char, count in freq_map.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                arr[index] = char
                index += 2
                count -= 1 

        return "".join(arr)    



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna