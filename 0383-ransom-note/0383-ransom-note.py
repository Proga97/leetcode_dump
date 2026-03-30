class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        for n in magazine:
            count[n] += 1
        for n in ransomNote:
            count[n] -= 1
            if count[n] < 0: return False

        return True

        