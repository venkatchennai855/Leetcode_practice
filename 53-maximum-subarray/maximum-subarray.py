class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-sys.maxsize-1
        summ=0
        for i in range(n):
            summ=summ+nums[i]
            maxi=max(summ,maxi)
            if(summ<0):
                summ=0
        return maxi





        return maxi