class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxy = 0
        for i in nums:
            if i == 1:
                count += 1
                maxy = max(maxy, count)
            else:
                count = 0
        return maxy
        