#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
// first find out what current idx water is derived from
// two pass solution -> two pointer solution
    int trap(vector<int>& height) {
        // the current trap is determined
        // by min(max_left, max_right) - heights[idx]
        int n = height.size();
        int l = 0, r = n - 1;
        int max_left = 0, max_right = 0, tmp = 0, rst = 0;
        // update the smaller one
        while(l < r){
            if(height[l] > height[r]){
                tmp = min(max_left, max_right) - height[r];
                if(tmp > 0) rst += tmp;
                max_right = max(max_right, height[r--]);
            }
            else{
                tmp = min(max_left, max_right) - height[l];
                if(tmp > 0) rst += tmp;
                max_left = max(max_left, height[l++]);
            }
        }
        return rst;
    }
};

int main(){
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    Solution s;
    cout<<s.trap(height)<<endl;
    return 0;
}