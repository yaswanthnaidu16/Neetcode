class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def get_second(x):
            return x[1]
        pairs.sort(key=get_second)
        ans = 0
        prev = float('-inf')
        for l, r in pairs:
            if l > prev:
                ans += 1
                prev = r
        return ans