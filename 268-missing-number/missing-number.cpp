class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int realsum=n*(n+1)/2;
        int sum;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        return (realsum-sum+1);
    }
};