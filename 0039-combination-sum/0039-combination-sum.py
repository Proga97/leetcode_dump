class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i , path, total):
            if total == target:
                res.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] <= target:
                    path.append(candidates[j])
                    dfs(j, path, total + candidates[j])
                    path.pop()

            return 
        
        dfs(0, [], 0)
        return res
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna