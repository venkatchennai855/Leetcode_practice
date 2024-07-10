class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=list(set(nums))
        arr.sort()
        leng=0
        maxlen=0
        if(len(arr)==0):
            return 0
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1]==1):
                leng+=1
                maxlen=max(leng,maxlen)
            else:
                leng=0
        return maxlen+1