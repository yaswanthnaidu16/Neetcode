class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a = 0
        for x in s:
            if a < len(t) and x == t[a]:
                a += 1
        return len(t) - a