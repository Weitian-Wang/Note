#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // dp[amount][idx] represents the min number of coins to add up to amount with coin_1-coin_idx
        // dp[amount][idx] 
        // = 
        // dp[amount][idx-1]   without current coin
        // +
        // dp[amount-idx][idx] with current coin
        vector<vector<int>> dp(amount+1);
        for(int i = 0; i <= amount; i++){
          dp[i] = vector<int>(coins.size());
        }
        for(int i = 0; i <= amount; i++){
            for(int j = 0; j < coins.size(); j++){
                if(i==0){
                    dp[0][j] = 1;
                    continue;
                }
                if(j==0){
                    dp[i][0] = i%coins[0]?0:i/coins[0];
                    continue;
                }
                dp[i][j] = (i-coins[j]>=0?dp[i-coins[j]][j]:0)+dp[i][j-1];
            }
        }
        for(int i = 0; i <= amount; i++){
            for(int j = 0; j < coins.size(); j++){
              cout<<dp[i][j]<<"  ";
            }
            cout<<endl;
        }
        return dp[amount][coins.size()-1];
    }
};

int main(){
  Solution s = Solution();
  int amount = 5;
  vector<int> coins = {1,2,5};
  s.change(amount, coins);
  cout<<!1<<endl;
  return 0;
}