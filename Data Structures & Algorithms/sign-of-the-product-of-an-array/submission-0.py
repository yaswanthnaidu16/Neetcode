class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 0
        pos = 0
        neg = 0
        for i in nums:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1
            else:
                return 0
        if pos == len(nums) or neg % 2 == 0:
            return 1
        else:
            return -1