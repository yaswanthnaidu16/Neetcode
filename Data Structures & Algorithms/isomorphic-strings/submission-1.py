class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        for i in range(len(s)):
            if s[i] in c1 and c1[s[i]] != t[i]:
                return False
            if t[i] in c2 and c2[t[i]] != s[i]:
                return False
            c1[s[i]] = t[i]
            c2[t[i]] = s[i]
        return True