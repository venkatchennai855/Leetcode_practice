class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        def genunique_sub(arr, ind, ans, ds):
            if ind == len(arr):
                ans.append(ds.copy())
                return
            # Include the element
            ds.append(arr[ind])
            genunique_sub(arr, ind + 1, ans, ds)
            ds.pop()
            # Skip duplicates
            while ind + 1 < len(arr) and arr[ind] == arr[ind + 1]:
                ind += 1
            # Exclude the element
            genunique_sub(arr, ind + 1, ans, ds)

        
        arr.sort()
        ans = []
        ds = []
        genunique_sub(arr, 0, ans, ds)
        ans.sort()
        return (ans)        