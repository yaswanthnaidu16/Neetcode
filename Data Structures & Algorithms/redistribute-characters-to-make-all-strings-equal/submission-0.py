class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        s = ""

        for i in words:
            s += i

        for i in set(s):
            if s.count(i) % n != 0:
                return False

        return True