from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        dic= defaultdict(list)
        for s in strs:
            count =  [0] * 26
            for c in s:
                count[ ord(c) - ord('a') ] += 1
            count = tuple(count)
            dic[count].append(s)
       
        return list(dic.values())
 


        