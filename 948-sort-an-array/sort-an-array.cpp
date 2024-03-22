class Solution {
public:
    void merge(vector<int>& a,int low, int mid, int high)
    {
        int i=low, j=mid+1;
        vector<int> b;
        while(i<=mid && j<=high)
        {
            if (a[i]<a[j]) 
            {
                b.push_back(a[i]);
                i++;
            }
            else 
            {
                b.push_back(a[j]);
                j++;
            }
        }
        while(i<=mid)
        {
            b.push_back(a[i]);
            i++;
        }
        while(j<=high)
        {
            b.push_back(a[j]);
            j++;
        }
        int k=0;
        for(int i=low;i<=high;i++)
        {
            a[i]=b[k++];
        }
    } 
    void mergesort(vector<int>& a,int low,int high)
    {
        if (low>=high) return;
        int mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,mid,high);
    }
    vector<int> sortArray(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        mergesort(nums,low,high);
        return nums;
        
    }
};