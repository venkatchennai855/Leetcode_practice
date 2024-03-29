class Solution {
public:
    void print(vector<int>& a, int n){
        for(int i=0; i<n; i++)
            cout<<a[i]<<',';
        cout<<endl;
    }
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> a(n, 1);
        //a[i]=product of nums[k] over k>i
        for(int i=n-2; i>=0; i--){
            a[i]=nums[i+1]*a[i+1];
        }
        //b=product of nums[k] over k<j
        int b=1;
        for(int j=1; j<n; j++){
            b*=nums[j-1];
            a[j]*=b;
        }
//        print(a, n);
        return a;
    }
};