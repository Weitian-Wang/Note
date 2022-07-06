- [Algorithm](#algorithm)
	- [Binary Search](#binary-search)
		- [Basic Version](#basic-version)
			- [Solution](#solution)
			- [Execution Details](#execution-details)
			- [Complexity](#complexity)
		- [Variant.1 First Bad Version](#variant1-first-bad-version)
			- [Solution](#solution-1)
		- [Variant.2 Rotated Sorted Array I](#variant2-rotated-sorted-array-i)
			- [Solution](#solution-2)
		- [Variant.3 Rotated Sorted Array II](#variant3-rotated-sorted-array-ii)
			- [Solution](#solution-3)
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
			- [Complexity](#complexity-1)
		- [Example.3 Coin Change](#example3-coin-change)
			- [Solution](#solution-4)
		- [Example.4 Longest Common Subsequence](#example4-longest-common-subsequence)
			- [Solution](#solution-5)
		- [Conclusion](#conclusion)
	- [Sort](#sort)
	- [Recursion](#recursion)
	- [Backtack](#backtack)
	- [Slide Window](#slide-window)
	- [Binary Search Tree](#binary-search-tree)
	- [Graph BFS DFS](#graph-bfs-dfs)
- [Data Structure](#data-structure)

# Algorithm
## Binary Search
### Basic Version
> [Leetcode: 704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an **sorted** (ascending) array of integer `nums` and a integer `target`, find the index of the target, or return -1 if non-existent.
#### Solution
1. Initial state:
- start / left / lo = 0
- end / right / hi = len(nums) **- 1**
    > Note: The end index of an array is length - 1.
2. Process:
- mid = (start + end)//2
  > Note:
  > 
  > In python3 use operator `//`, or use `/` in python2 between two integers.  
  >
  > Or use math library to floor devision result:  
  > `mid = math.floor((start+end)/2)`  
  > 
  > This trick gets around integer overflow in C/C++:  
  > `mid = start + (end-start)//2`  
- Condition: compare `nums[mid]` to `target`
   - if `target` == `nums[mid]`: found index `mid` 
   - if `target` > `nums[mid]`: search latter half of the array
   - if `target` < `nums[mid]`: search first half of the array
3. Repeat: 
    Loop until start and end converge, or found index in process.
#### Execution Details
1. Shrink Boundary & Exit Condition  
- Include `mid`
   - Loop condition: `while start+1 < end`
        > Note: Regardless of array having even or odd number of elements, `start` and `end` will converge to **two** consecutive indexes.  
        >  ```
        >  Case.1 Even                          Case.2 Odd
        >  -------------------------            ----------------------
        >  target   6                           target   4        
        >  index    0  1  2  3  4  5            index    0  1  2  3  4      
        >  array   -1  0  1  2  4  6            array   -1  0  1  2  4
        >           ▲     ▲        ▲                     ▲     ▲     ▲
        >  it-1   start  mid      end           it-1   start  mid   end
        >                 ▲  ▲     ▲                           ▲  ▲  ▲
        >  it-2           s  m     e            it-2           s  m  e
        >                    ▲  ▲  ▲                              ▲  ▲
        >  it-3              s  m  e            it-3              s  e
        >                       ▲  ▲                              ▲  ▲
        >  it-4                s/m e            it-4             s/m e
        >  ```
        >  In cases like the 4th iteration, we'll stuck in infinite loop.
    
   - Shrink end: `end = mid`
   - Shrink start: `start = mid`
   - After loop: Check last **two** elements, `nums[start] == target` or `nums[end] == target`
- Exclude `mid`
    - Loop condition: `while start < end`, exit when start and end converge `start == end`
        > Note: Because of excluding mid, `start` and `end` will converge to same value.
    - Must check `if nums[mid] == target` before shrinking boundaries.
    - Shrink end: `end = mid - 1`
    - Shrink start: `start = mid + 1`
    - After loop: Check the **last** element, `nums[start or end] == target`
2. Recursion or While Loop  
   Obviously, any subarray of a sorted array is also sorted. Locating `target` in first or latter half of orginal array is a subquestion, therefore we can also use recursion.
    > Note: Subarray vs Subsqeuence vs Subset  
    > Consider an array [1, 2, 3, 4]  
    > Subarray: Contiguous and retains order, [2, 3, 4]  
    > Subsequence: Only maintain relative order, [1, 3, 4]  
    > Subset: Neither contiguous nor in relative order, [4, 1, 3]  
    > ```
    > ┌─────────────────────────────────┐
    > │ Subset                          │
    > │    ┌───────────────────────┐    │
    > │    │ Subsequence           │    │
    > │    │   ┌───────────────┐   │    │
    > │    │   │               │   │    │
    > │    │   │   Subarray    │   │    │
    > │    │   │               │   │    │
    > │    │   └───────────────┘   │    │
    > │    └───────────────────────┘    │
    > └─────────────────────────────────┘
    > ```
    However, while recursion is easier to understand and to implement, it's slower than iteration (at least in Java, C and Python).
#### Complexity
The solution eliminates half of the array at each iteration, until converge to a single element.
$$ 2^{\text{iteration}}=n $$
$$ \text{iteration}\ =\ \log_2 n$$
1. Average: $O(\log n)$  
2. Best-case: When the target is in the middle of array, $O(1)$.
3. Worst-case: When the target is at either extremity of the array, the solution will go through all $\log_{2}{n}$ iterations.
   > Note: $\log_{a}{b}$ is pronounced "log base `a` of `b`".
### Variant.1 First Bad Version
> [Leetcode: 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)  

Instead of sorted list, we have `n` versions `[1, 2, 3, ..., n]`, objective is to find the first bad one which all following ones are bad. 
```
Ver.No   1  2  3  4  ...  n-1  n
Status   ✓  ✓  ✕  ✕  ...   ✕   ✕
               ▲
              this
```
#### Solution
1. Initial State
 - start =  1 
 - end = n
2. Process
    > Note: An implementation of binary search, using **include mid** method. 

 - Loop condition: start + 1 < end
 - `mid` = `(start+end)//2`
 - Condition:
   - if `isBadVersion(mid)`: shrink end point
   - if `not isBadVersion(mid)`: shrink start point
3. Repeat:  
Until start and converge to two contiguous versions.
- Scenario 1: `if isBadVersion(start)`, in this case 1st version is bad.
- Scenario 2: `else`, `end` is the 1st bad version, with its previous version good. 
### Variant.2 Rotated Sorted Array I
> [Leetcode: 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Given an ascending integer array `nums` with **distinct** values, rotated at random point (doesn't matter where). E.g. `[0, 1, 2, 4, 5, 6, 7]` after rotation became `[4, 5, 6, 7, 0, 1 ,2]`. Find index of integer `targe` if its in `nums`, or -1 if it is not in the array.

#### Solution
1. Prerequisite:  
- The rotated sorted array is partially sorted.
    ```
    4  5  6  7  0  1  2
    ----------  -------
       left      right
    ```
- The subarray of rotated sorted array is also rotated sorted.
    ```
    6  7  0  1  2
    ----  -------
    left   right
    ```
2. Is start-mid part sorted? Or is mid-end part sorted?
    > Note: Compare `nums[mid]` to `nums[end]`, where `nums[end]` is the last element of the smaller subarray.
    > 
    > ```
    > index 0  1  2  3  4  5  6             index 0  1  2  3  4  5  6
    > nums  4  5  6  7  0  1  2             nums  6  7  0  1  2  3  4
    >       ----------  -------                   ----  -------------
    >          left      right                    left       right
    >       ▲        ▲        ▲                   ▲        ▲        ▲
    >       │        │        │                   │        │        │
    >     start     mid      end                start     mid      end
    > ```
3. Is target in sorted subarray?  
    - target in sorted subarray: regular binary search  
    - target not in sorted part: subquestion of original question
        > Subarray of a rotated sorted array is also rotated sorted.
4. Full logic (Decision Tree)
    ```
                               ┌─────────┐
                               │ target  │
                            ┌─►│ in      ├───► binary search - shrink end
               ┌─────────┐  │  │ left    │
               │ left    │  │  └─────────┘
            ┌─►│ part    ├──┤
            │  │ sorted  │  │  ┌─────────┐
            │  └─────────┘  │  │ target  │    
            │               └─►│ not in  ├───► subquestion - shrink start
            │                  │ left    │   
            │                  └─────────┘
    begin───┤
            │                  ┌─────────┐
            │                  │ target  │    
            │               ┌─►│ in      ├───► binary search - shrink start
            │  ┌─────────┐  │  │ right   │
            │  │ right   │  │  └─────────┘
            └─►│ part    ├──┤
               │ sorted  │  │  ┌─────────┐
               └─────────┘  │  │ target  │    
                            └─►│ not in  ├───► subquestion - shrink end
                               │ right   │
                               └─────────┘
    ``` 

### Variant.3 Rotated Sorted Array II
> [Leetcode: 81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

Based on question [Variant.2](#variant2-rotated-sorted-array-i), but the elements can be the same (**not** necessarily **distinct**).
```
  index    0  1  2  3  4  5
  array   -1  0  0  1  2  2
```
#### Solution
Same method can be used when tackling this problem, but with one exceptional case, which was shown as following diagram.
```
index    0  1  2  3  4  5                 index    0  1  2  3  4  5
array    1  1  1  2  1  1                 array    1  2  1  1  1  1
         ----------  ----                          ----  ----------
            left     right                         left     right
         ▲     ▲        ▲                          ▲     ▲        ▲
         │     │        │                          │     │        │
       start  mid      end                       start  mid      end
```
Which part (start-mid or mid-end part) is sorted is no longer be determined by the relationship between `nums[mid]` and `nums[end]`. This problem is solely caused by **intial** and **trailing** duplicated elements. Skip them before [this](#solution-2) process.
```python
start = 0
end = len(nums) - 1
while start < end and nums[start] == nums[start+1]:
    start += 1
while start < end and nums[end] == nums[end-1]:
    end -= 1
```

## Dynamic Programming
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
    # index 0 to n
	# !IMPORTANT!
    # range(start, end) -> [start, end) -> s, s+1, ..., e-2, e-1
    # range(end) -> [0, end) -> 0, 1, ..., end-1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    ```
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
`text1` = $\{a_1, a_2, a_3, ..., a_m\}$  
`text2` = $\{b_1, b_2, b_3, ..., b_n\}$  
where `m` and the length of `text1` and `n` is length of `text2`.  
	> Note: Be careful about dimensions and indices, start from 0 or 1.  

2. Define 2-D DP Array  
Define `DP[m+1][n+1]`.  
`DP[i][j]` represents the length of LCS between $\{a_1, a_2, a_3, ..., a_i\}$ and $\{b_1, b_2, b_3, ..., b_j\}$, which is the first `i` and `j` characters of `text1` and `text2` respectively.
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
### Conclusion
start from brute force (**recursive**, decision tree), then optimize top down with memorization, then come up with bottom up dynamic programming technique.  

## Sort
## Recursion
## Backtack
## Slide Window
## Binary Search Tree
## Graph BFS DFS
# Data Structure
