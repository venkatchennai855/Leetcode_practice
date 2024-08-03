class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1  
        while(i<j):
            x=numbers[i]+numbers[j]
            if(x==target):
                return[i+1,j+1]
            if(x>target):
                j=j-1
            if(x<target):
                i=i+1 
        