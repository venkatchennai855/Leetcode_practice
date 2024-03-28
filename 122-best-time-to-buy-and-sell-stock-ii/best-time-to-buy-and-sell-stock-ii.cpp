class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int r=1;
        int p=0;
        int mp=0;
        int sum=0;
        while(r<prices.size()){
            if(prices[l]<prices[r]){
                p=prices[r]-prices[l];
                sum+=p;
                l++;
            }
            else{
                l=r;
            }
            r++;

        }
        return sum;
    }
};