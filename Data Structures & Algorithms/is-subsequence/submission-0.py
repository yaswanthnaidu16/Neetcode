class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(reversed(s))
        
        for char in t:
            if not stack:
                return True

            if char == stack[-1]:
                stack.pop()

        return not stack