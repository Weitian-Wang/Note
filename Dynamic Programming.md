## Dynamic Programming
- [Dynamic Programming](#dynamic-programming)
  - [Introduction](#introduction)
    - [Characteristics of DP Problems](#characteristics-of-dp-problems)
    - [DP vs. Recursion](#dp-vs-recursion)
    - [DP vs. Devide & Conquer](#dp-vs-devide--conquer)
  - [Example.1 Fibonacci Numbers](#example1-fibonacci-numbers)
    - [Solution.1 Bottom-Up with Tabulation (DP)](#solution1-bottom-up-with-tabulation-dp)
    - [Solution.2 Top-Down with Memorization (Recursion)](#solution2-top-down-with-memorization-recursion)
  - [Example.2 0/1 Knapsack](#example2-01-knapsack)
    - [Solution.1 Basic Brute Force](#solution1-basic-brute-force)
    - [Solution.2 Dynamic Programming](#solution2-dynamic-programming)
    - [Complexity](#complexity)
  - [Example.3 Coin Change](#example3-coin-change)
    - [Solution](#solution)
  - [Example.4 Longest Common Subsequence](#example4-longest-common-subsequence)
    - [Solution](#solution-1)
  - [Example.5 Best Time to Buy and Sell Stock with Cooldown](#example5-best-time-to-buy-and-sell-stock-with-cooldown)
    - [Solution.1 Top-Down Recursion](#solution1-top-down-recursion)
    - [Solution.2 Bottom-Up Dynamic Prog](#solution2-bottom-up-dynamic-prog)
  - [Conclusion](#conclusion)

### Introduction
Dynamic Programming (DP) is a algorithmic technique for solving an optimization problem, where we break down the original problem into smaller subproblems.
> Note:  
> Optimization Problem: The problem of finding the best solution from all feasible solutions.  
> Subproblem: Smaller version (smaller ```n```) of the original problem.
#### Characteristics of DP Problems
The following characteristics in a problem indicates that we can apply Dynamic Programming for problem solving.
1. Overlapping Subproblems  
To solve the original problem, the same subproblem is solved multiple times.
2. Optimal Substructure  
Overall optimal solution can be constructed from the solutions of its subproblems. 
#### DP vs. Recursion
#### DP vs. Devide & Conquer
### Example.1 Fibonacci Numbers
> [Leetcode: 509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
The Fibonacci numbers, denoted as F(n) form a Fibonacci sequence. Any number in the sequence is the sum of two preceeding ones `F(n)=F(n-1)+F(n-2)`, starting from `F(0)=0` and `F(1)=1`. Given `n`, calculate `F(n)`.
```
F(4)  =  F(3)    +    F(2)
           ▲            ▲
           │            │
      F(2) + F(1)  F(1) + F(0)
        ▲
        │
   F(1) + F(0)
```
#### Solution.1 Bottom-Up with Tabulation (DP)
> Note: DP Indicators  
> 1. Overlapping Subquestions, as F(1) and F(0) are calculated multiple times.  
> 2. Optimal Substructure, as The solution F(n) can be composed with subquestion F(n-1) and F(n-2).  
1. Initial State  
Start from smallest subproblems, F(0) and F(1).
    ```python
    dp = [0 for i in length(n+1)]
    dp[0] = 0
    dp[1] = 1
    ```
2. Process  
    Calculate number at next position, store results of subproblems in DP array.
    ```python
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    ```
    > Note: Builtin `range` Function in Python  
    > `range(start, end)` -> [start, end) -> s, s+1, ..., e-2, e-1  
    > `range(end)` -> [0, end) -> 0, 1, ..., end-1  
3. Repeat  
    Repeat until reach n-th Fiboncci number.  
4. Comlexity and optimization  
    Time complexity O(n), extra space O(n).  
    By storing only previous two numbers, we can achieve O(1) extra space.
    ```python
    # a = F(n-2), b = F(n-1)
    c = a + b
    a = b
    b = c
    ```
#### Solution.2 Top-Down with Memorization (Recursion)
1. Define Recursive Function  
    `fibonacci(n)`
2. Exit Condition
    * `n==0`, `return 0`  
    * `n==1`, `return 1`
3. Recursive Call  
`return fibonacci(n-1) + fibonacci(n-2)`
4. Complexity and optimization  
    > [Complexity Analysis](https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/)
    ```
              Recursion Tree            Call Stack Depth
                                             ┌───┐
                   fib(4)                    │ 1 │
                 /        \                  ├───┤
             fib(3)      fib(2)              │ 2 │
            /    \       /    \              ├───┤
      fib(2)   fib(1)  fib(1) fib(0)         │ 3 │
      /     \                                ├───┤
    fib(1) fib(0)                            │ 4 │
                                             └───┘
    ```
    Same subproblem is solved multiple times, for example fib(2) called twice.  
    We can store solved subproblem (memorization) and skip nodes on recursion tree.
    ```
        Optimized Recursion Tree
                     fib(4)
                   /        \
               fib(3)      fib(2)
              /    \
         fib(2)   fib(1)
        /     \
       fib(1) fib(0)
    ```
### Example.2 0/1 Knapsack
> Note: 0/1 Knapsack problem, with weight limit.  

Given the weights and profits of `N` items, put these items in a knapsack that has capacity `C`. Goal is to get max profit from items in the knapsack. Each item can only be selected **once**.  
Example:  
```
Items      A   B   C   D
Weights  { 2   3   1   4 }
Profits  { 4   5   3   7 }
Capacity   5 (weight units)
```
The most profitable combination would be item C + D, with a total weight of 5, which generates 10 profit.  
#### Solution.1 Basic Brute Force  
1. Idea  
Try every combination of all items, then choose one combination with maximum profit under weight limit.  
1. Decision tree:
    ```
                         weight: 0                    
                         profit: 0                    
                       /           \
                      A            nA
                     /               \
               weight: 2           weight: 0          # deepth: n + 1
               profit: 4           profit: 0          # total no. nodes: 2^(n+1)-1
              /         \                             # asymptotic complexity: O(2^n)
             B          nB                            # 2^n: two to the power of n
            /             \
     weight: 5          weight: 2     ...
     profit: 9          profit: 4
    ```  
2. Recurrence relation:  
    $F(\{A, B, C, D\}, W)$ represents the maximum profit of item {A, B, C, D} under weight limit W, is the larger value of:
    * the solution includes item A
    * the solution excludes item A
	$$ F(\{A, B, C, D\}, W)\ =\ MAX(F(\{B, C, D\}, W-W_A) + P_A,\ F(\{B, C, D\}, W)) $$
	This shows the characteristic of Optimal Substructure.
3. Code:   
    ```python
    def knapsack(profits, weights, capacity, index):
        if index ==  len(profits) or capacity <= 0:
            return 0
        profit1 = 0
        if capacity >= weights[index]:
            # the part contains current item
            profit1 = profits[index] + knapsack(profits,
                                                weights,
                                                capacity - weights[index],
                                                index + 1)
        # the solution excludes current item
        profit2 = knapsack(profits, weights, capacity, index + 1)
        return max(profit1, profit2)
    ```
4. Overlapping subproblem:  
    By logging each call of the function, we can find function was called twice with identical arguments (overlapping subproblem). The number of duplicated calls will increase as number of items increase. Therefore we can use Memorization to optimize. The optimized complexity would be $O(N\times C)$, where N is the nuber of items, C is the capacity.
    ```
    call:1 capacity:1 skipped:3 profit:0
    call:2 capacity:4 skipped:3 profit:0    <----- duplicated
    ...
    call:10 capacity:5 skipped:2 profit:16
    call:11 capacity:4 skipped:3 profit:0   <----- duplicated
    ...
    call:15 capacity:7 skipped:0 profit:22
    ```
#### Solution.2 Dynamic Programming  
1. Idea  
    Define 2-D array `dp[N][C+1]`, as used in optimized [solution.1](#solution1-basic-brute-force). `dp[i][c]` will represent the maximum knapsack profit for capacity `c` calculated from the **first `i` items** (item 0 to i).  
    > Note: The key is to understand the meaning of `dp[i][c]`, and the relation with previous elements.  
    For each `i` and `c`, we choose the maximum from two options:  
    1. Exclude current item, use previous profit: `dp[i-1][c]`
    2. Include current item, plus previous profits with current weight subtracted: `profits[i] + dp[i-1][c-weights[i]]`  

    Fill out all array in **bottom up** fashion, from left to right, row by row. The `dp[N][C]` would be the solution to the original problem.  
2. Initial dp array:  
    ```
                                      capacity
                            0   1   2   3   4   5   6   7
    profit  weight  index ┌───┬───┬───┬───┬───┬───┬───┬───┐
      4       2       0   │ 0 │   │   │   │   │   │   │   │
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      5       3       1   │ 0 │   │   │   │   │   │   │   │
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      3       1       2   │ 0 │   │   │   │   │   │   │   │
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      7       4       3   │ 0 │   │   │   │   │   │   │   │
                          └───┴───┴───┴───┴───┴───┴───┴───┘
    ```
3. Completed dp array:  
    ```
                                      capacity
                            0   1   2   3   4   5   6   7
    profit  weight  index ┌───┬───┬───┬───┬───┬───┬───┬───┐
      4       2       0   │ 0 │ 0 │ 4 │ 4 │ 4 │ 4 │ 4 │ 4 │
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      5       3       1   │ 0 │ 0 │ 4 │ 5 │ 5 │ 9 │ 9 │ 9 │
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      3       1       2   │ 0 │ 3 │ 4 │ 7 │ 8 │ 9 │ 12│ 12│
                          ├───┼───┼───┼───┼───┼───┼───┼───┤
      7       4       3   │ 0 │ 3 │ 4 │ 7 │ 8 │ 10│ 12│ 14│
                          └───┴───┴───┴───┴───┴───┴───┴───┘
    ```
4. Code:  
    ```python
    def knapsack(profits, weights, capacity):
        # define 2D array dp, initialize first column
        dp = [[0]*(capacity+1) for i in range(len(profits))]
        for i in range(len(profits)):
            for c in range(1, capacity+1):
                # fill out first row
                if i == 0:
                    dp[i][c] = profits[i] if c>= weights[i] else 0
                else:
                    profit1 = 0
                    if c - weights[i]>=0:
                        profit1 = dp[i-1][c-weights[i]]+profits[i]
                    profit2 = dp[i-1][c]
                    dp[i][c] = max(profit1, profit2)
                # one-liner
                # dp[i][c] = max(dp[i-1][c-weights[i]]+profits[i] if c-weights[i]>=0 else 0, dp[i-1][c])
        return dp[len(profits)-1][capacity]
    ```
#### Complexity  
1. Brute Force  
    For a recursive problem with recurrence relation like $F(n)=\begin{cases}F(n-1)\newline F(n-2)\end{cases}$, the time complexity using brute force is $O(2^{n+1}-1)$, which is asymptotically equivalent to $O(2^n)$. Space complexity $O(n)$ is the depth of recursion stack. 
    > Note:
    > Decision tree is a **perfect binary tree** of depth `n`.  
    > Number of nodes is $S_n\ =\ \frac{a_1(1-r^n)}{1-r} = 2^{n+1}-1$   
> Note: Types of Binary Tree  
> 1. Full Binary Tree: Every node have 0 or 2 children.
> 2. Complete Binary Tree: All levels have complete nodes, except for last level. Nodes on the last level are as left side as possible.
> 3. Perfect Binary Tree: All nodes except leaf nodes have two children and leaf nodes are at same depth.  
> Note: Common Types of Sequence
> 1. Arithmetic Sequence: An arithmetic sequence has a **constant difference** between each consecutive pair of terms.
> 2. Geometic Sequence: A geometric sequence has a **constant ratio** between each consecutive pair of terms.
2. Optimized  
    After optimization, Memorization (top-down) or DP-Tabulation (bottom-up) has a space & time complexity of $O(N\times C)$, where $N$ represent total items and $C$ is the maximum capacity. 
### Example.3 Coin Change
> [Leetcode: 322. Coin Change](https://leetcode.com/problems/coin-change/)  
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing target amount of money. Return the **minimum** number of coins needed to make up that amount. If the total amount can not be made up by any combination of coins, return -1. Each coin can be used infinite times.  
Example:  
```
coins = [1,2,5], amount = 11
return 3
explain 11 = 5 + 5 + 1
```
#### Solution
1. Brute Force  
	Recurrence Relation:  
	$$ coins = \{c_1,\ c_2,\ ...,\ c_n\} $$
	$$ F(a) = MIN(F(a-c_1)+1,\ F(a-c_2)+1,\ ..., F(a-c_n)+1) $$
	> Note: F(a) represents minimum number of coins needed to make up to amount `a`.  
	Recursion Tree:  
	```
	                ┌───┐
	amount          │ 11│
	                └───┘
	              /   |   \
	coin used    1    2    5
	            /     |     \
	         ┌───┐  ┌───┐  ┌───┐
	remain   │ 10│  │ 9 │  │ 6 │
	         └───┘  └───┘  └───┘
	         / | \
	        1  2  5       ...
	       /   |   \
	   ┌───┐ ┌───┐ ┌───┐
	   │ 9 │ │ 8 │ │ 5 │
	   └───┘ └───┘ └───┘
	    ...
	```
	For each remaining amount, use coins of different denominations, until the remaining amount is 0. The minimum **depth** of all leaves with value 0 is solution. To get every possible combination, recursion was executed in DFS manner. As F(9) was solved multiple times, overlapping subproblems exist in this problem.
2. Optimize with Memorization  
	Store calculated value in 1D array DP.
3. Bottom Up Dynamic Programming  
	Fill the 1-D DP array from bottom up, according to the recurrence relation.
	```
	coins {1,4,5}
	index 0 1 2 3 4 5 6 7 8 9
	     ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
	 DP  │0│ │ │ │ │ │ │ │ │ │
	     └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
	```
	```python
	MAX = float('inf')
    DP = [0] + [MAX]*amount
    for a in range(1, amount+1):
        DP[a] = min([DP[a-c]+1 if a-c>=0 else MAX for c in coins])
	return -1 if DP[amount]==MAX else DP[amount]
	```
	> Note: Trick  
	> We can set `MAX = amount + 1`.
### Example.4 Longest Common Subsequence
> [Leetcode: 1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
Given two strings `text1` and `text2`, return the length of their longest common subsequence.  
Example:  
```
text1 = "abcde"
text2 = "ace" 
=> longest common subsquence = "ace", length = 3
```  
#### Solution
1. Mathematical Notation  
`text1` = $[\ a_1, a_2, a_3, ..., a_m\ ]$  
`text2` = $[\ b_1, b_2, b_3, ..., b_n\ ]$  
where `m` and the length of `text1` and `n` is length of `text2`.  
	> Note: Be careful about dimensions and indices, start from 0 or 1.  
2. Define 2-D DP Array  
Define `DP[m+1][n+1]`.  
`DP[i][j]` represents the length of LCS between $[\ a_1, a_2, a_3, ..., a_i\ ]$ and
$[\ b_1, b_2, b_3, ..., b_j\ ]$, which is the first `i` and `j` characters of `text1` and `text2` respectively.
	```
	\j
	i\   0   1   2   3            i
	   ┌───┬───┬───┬───┐          │
	0  │ 0 │ 0 │ 0 │ 0 │          ▼
	   ├───┼───┼───┼───┤    text1 a b c d e
	1  │ 0 │ 0 │ 0 │ 0 │          1 2 3 4 5
	   ├───┼───┼───┼───┤
	2  │ 0 │ 0 │ 0 │ 0 │
	   ├───┼───┼───┼───┤
	3  │ 0 │ 0 │ 0 │ 0 │          j
	   ├───┼───┼───┼───┤          │
	4  │ 0 │ 0 │ 0 │ 0 │          ▼
	   ├───┼───┼───┼───┤    text2 a c e
	5  │ 0 │ 0 │ 0 │ 0 │          1 2 3
	   └───┴───┴───┴───┘
	```
3. Relation Function  
Fill out DP array according to the following rule:  
* if $a_i$ == $b_j$, `dp[i][j] = dp[i-1][j-1] + 1`
* else `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`  
4. Completed DP Array  
`dp[m][n]` is the solution of the original problem.
	```
	\j
	i\   0   1   2   3                    i
	   ┌───┬───┬───┬───┐                  │
	0  │ 0 │ 0 │ 0 │ 0 │                  ▼
	   ├───┼───┼───┼───┤    text1 a b c d e
	1  │ 0 │ 1 │ 1 │ 1 │          1 2 3 4 5
	   ├───┼───┼───┼───┤
	2  │ 0 │ 1 │ 1 │ 1 │
	   ├───┼───┼───┼───┤
	3  │ 0 │ 1 │ 2 │ 2 │              j
	   ├───┼───┼───┼───┤              │
	4  │ 0 │ 1 │ 2 │ 2 │              ▼
	   ├───┼───┼───┼───┤    text2 a c e
	5  │ 0 │ 1 │ 2 │ 3 │          1 2 3
	   └───┴───┴───┴───┘
	```
### Example.5 Best Time to Buy and Sell Stock with Cooldown
> [Leetcode: 309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)  

Given an array `prices` where `prices[i]` is the price of a given stock on the i-th day. Find the maximum profit you can achieve with restrictions:  
* unlimited number of transactions (buy and sell this stock as many times as you like)
* one day of cooldown after sell (can not buy next day after sell)
* must sell before buy again (may not engage in multiple transactions)

Example:
```
prices = [1, 2, 3, 0, 2]            prices = [3, 2, 1, 0, 2]
action    b  s  c  b  s             action    c  c  c  b  s
max_profit = 3                      max_profit = 2
```
> Note: Coding Detail  
> To make notation of day and index of array consistant, day start from 0.

#### Solution.1 Top-Down Recursion
1. Idea: Find Recurrence Relation  
    Let `F(i)` represent the maximum profit achievable at `i`-th day.
    Any day can be a  
    1. Buy day: max profit equals to last day's  
        `F(i) = F(i-1)`
    2. Cooldown day: max profit equals to last day's  
        `F(i) = F(i-1)`
    3. Sell day: `j` denotes the corresponding buy date of sell day `i`  
        The max profit from sell day `i` is the composed of two parts:  
        * Profit from this sell  
        `profits[i] - profits[j]`

        * Profit from previous sells   
        `F(j-2)`  
            > Explanation:  
            > As `j` is an buy day, `j-1` must be a cooldown day, which can not generate profit. Skip `j-1` directly to `j-2` to ensure not profit was made in `j-1`th day.

        Therefore the maximum sell day profit:  
        `F(i) = profits[i] - profits[j] + F(j-2)` for each `j` before `i`

    The final profit is the maximum of the listed three parts: 
    $$F(i)\ =\ max(F(i_{buy}),\ F(i_{cooldown}),\ F(i_{sell}))$$  

2. Implement with Code
    ```python
    def maxProfitRecur(profits, index):
        # no profit before the first day
        if index<=0:
            return 0
        else:
            return max(maxProfitRecur(profits, index-1), max([maxProfitRecur(profits, j-2)+profits[index]-profits[j] for j in range(index)]))
    ```
#### Solution.2 Bottom-Up Dynamic Programming
Now that we've understanded the recurrence relation, we can optimize the solution with DP. 
1. Define DP Array  
`dp[i]` represents the maximum possible profit at `i`-th day.
2. Initial State
On the `0`th day, no complete transaction can be made, `dp[0] == 0`.  
3. Fill Out DP Array  
To help understand this process, take a look at the iteration where `i == 2`, and **potential** buy day `j == 0`.   
    ```
    prices = [1, 2, 3, 0, 2] 
    profit = [0, 1, 0, 0, 0]  <- DP Array
              ▲     ▲
              j     i
    ```
    `j-2` is smaller than `0`, which means no previous transactions has been completed, thus `dp[j-2] = 0`.  

### 
### Conclusion
start from brute force (**recursive**, decision tree), then optimize top down with memorization, then come up with bottom up dynamic programming technique.  

