class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int r=l+1;
        int n=prices.size();
        int p=0;
        int mp=0;
        while(r<n){
        
            if(prices[l]<prices[r]){
                p=prices[r]-prices[l];
                mp=max(p,mp);
            }
            else {l=r;}
            r++;
        }
        return mp;
    }
};