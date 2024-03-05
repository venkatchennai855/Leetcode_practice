class Solution {
public:
    int minimumLength(string s) {
        int l=0;
        int r=s.length()-1;
        while(l<r and s[l]==s[r]){
            char left=s[l];
            while(l<=r && s[l]==left){
                l++;
            }
            while(l<=r && s[r]==left){
                r--;
            }
            
        }
        return r-l+1;
    }
};