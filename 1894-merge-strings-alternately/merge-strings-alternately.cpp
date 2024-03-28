class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n=word1.size();
        int m=word2.size();
        vector<char> strg;
        int i=0;
        while((i<n) && (i<m)){
            strg.push_back(word1[i]);
            strg.push_back(word2[i]);
            i++;
        }
        while(i<n){
            strg.push_back(word1[i]);
            i++;
        }
        while(i<m){
            strg.push_back(word2[i]);
            i++;
        }
        string str(strg.begin(),strg.end());
        return str;

    }
};