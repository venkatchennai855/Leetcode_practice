class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def conseq(arr,index,target,ans,ds):
            if(index==len(arr)):
                if target==0:
                    ans.append(ds.copy())
                return
            if(target>=arr[index]):
                ds.append(arr[index])
                conseq(arr,index,target-arr[index],ans,ds)
                ds.pop(len(ds)-1)
            conseq(arr,index+1,target,ans,ds)
        ans=[]
        ds=[]
        conseq(arr,0,target,ans,ds)  
        return ans
