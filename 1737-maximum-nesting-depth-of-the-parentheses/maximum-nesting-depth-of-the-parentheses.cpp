class Solution {
public:
    int maxDepth(std::string s) {
        
        int depth = 0;
        int count = 0; 
        

        for (char ch : s) {

            if (ch == '(') {
                count++;
                depth = std::max(depth, count);
            }


            if (ch == ')') {
                count--;
            }
        }
        
        // Return the maximum depth found.
        return depth;
    }
};