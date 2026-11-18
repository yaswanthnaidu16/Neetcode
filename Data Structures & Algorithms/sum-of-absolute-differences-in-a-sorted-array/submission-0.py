class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=sum(nums)
        l=0
        res=[]
        for i in range(n):
            r=s-l-nums[i]
            a=nums[i]*i-l
            b=r-nums[i]*(n-i-1)
            res.append(a+b)
            l+=nums[i]
        return res