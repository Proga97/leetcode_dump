class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        w_length = len(words[0])
        w_map = Counter(words)
        req = len(words)
        res = []
        
        for i in range (len(s) - req * w_length + 1):
            seen = defaultdict(int)
            for j in range(i, i + req * w_length, w_length):
                word = s[j:j+w_length]

                if word not in w_map: break
                
                seen[word] += 1

                if seen[word] > w_map[word]: break
                # print(i, seen)
                if seen == w_map: 
                    res.append(i)
        return res



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna