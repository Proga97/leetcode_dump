class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        l = 0
        # r = 1
        res = set()
        size = 1

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1

            res.add(s[r])
            size = max(size,len(res))    

        # while r < len(s):
        #     # print(l,r,s[l],res,s[r])
        #     if s[r] in res:
        #         size = max(size,len(res))
        #         if l + 1 < r:
        #             l += 1
        #         else:
        #             l += 1
        #             r += 1
        #         res.remove(s[l-1])
        #         if len(res) == 0:
        #             res.add(s[l])
        #     else:
        #         res.add(s[r])
        #         r+=1
        return max(size,len(res))


        


        