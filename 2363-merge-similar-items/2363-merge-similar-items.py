class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        val_map = defaultdict(int)
        for val, weight in items1:
            val_map[val] += weight
        for val, weight in items2:
            val_map[val] += weight
            
        res = []
        for val, weight in val_map.items():
            res.append([val, weight])
        
        res.sort()
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna