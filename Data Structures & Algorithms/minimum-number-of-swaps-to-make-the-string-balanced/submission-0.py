class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '[':
                stack.append(i)
            elif stack:
                stack.pop()
        return (len(stack) + 1) // 2
