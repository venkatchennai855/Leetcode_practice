class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi = -sys.maxsize - 1
        sum=0
        for i in range(n):
            if(sum<0):
                sum=0
            sum=sum+nums[i]
            maxi=max(maxi,sum)


        return maxi