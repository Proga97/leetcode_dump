class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnesIdx, maxOnesCount = 0, 0  
        for i in range(len(mat)):
            ones = sum(mat[i])
            if ones > maxOnesCount:
                maxOnesCount = ones
                maxOnesIdx = i

        return [maxOnesIdx, maxOnesCount]  