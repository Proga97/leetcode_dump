class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for s in "balon":
            count[s] = 0
        for s in text:
            if s in count:
                count[s] += 1
        
        c_b = count['b']
        c_a = count['a']
        c_l = count['l']//2
        c_o = count['o']//2
        c_n = count['n']
        return min(c_a,c_b,c_l,c_o,c_n)

