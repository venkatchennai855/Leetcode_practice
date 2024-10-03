import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-sys.maxsize-1
        sum=0
        for i in nums:
            sum=sum+i
            maxi=max(maxi,sum)
            if(sum<0):
                sum=0
 
                

        return maxi
        