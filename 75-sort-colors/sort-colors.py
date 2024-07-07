class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        c0=0
        c1=0
        c2=0
        for i in range(n):
            if(nums[i]==0):
                c0+=1
            elif(nums[i]==1):
                c1+=1
            else:
                c2+=1
        for i in range(n):
            if(i<c0):
                nums[i]=0
            elif( i<c1+c0):
                nums[i]=1
            else:
                nums[i]=2

        