def knapsack(profits, weights, capacity):
    dp = [[0]*(capacity+1) for i in range(len(profits))]
    for i in range(len(profits)):
        for c in range(1, capacity+1):
            if i == 0:
                dp[i][c] = profits[i] if c>= weights[i] else 0
            else:
                dp[i][c] = max(dp[i-1][c-weights[i]]+profits[i] if c - weights[i]>=0 else 0, dp[i-1][c])
    for row in dp:
        print(row)
    return dp[len(profits)-1][capacity]

profits = [4, 5, 3, 7]
weights = [2, 3, 1, 4]
capacity = 7
print(knapsack(profits, weights, capacity))    