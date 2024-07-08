class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        ele=arr[0]
        count=1

        #moore's counting
        for i in range(1,n):
            if (count==0):
                ele=arr[i]
                count=1
            else:
                if(arr[i]==ele):
                    count=count+1
                else:
                    count=count-1

        #Verification
        if(arr.count(ele)>(n/2)):
            
            return ele


        # TC: O(N)
        # SC: O(1)