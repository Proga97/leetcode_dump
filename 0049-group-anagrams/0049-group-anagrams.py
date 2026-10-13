from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        hashmap = defaultdict(list)

        for s in strs:
            char_count = [0] * 26

            for ch in s:
                char_count[ord(ch)-ord("a")] += 1

            hashmap[tuple(char_count)].append(s)

        res = []
        for val in hashmap.values():
            res.append(val)
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna