class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i],0) + 1
            m[t[i]] = m.get(t[i],0) - 1
        for x in (m.values()):
            if x != 0:
                return False
        return True
