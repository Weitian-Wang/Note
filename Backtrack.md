## Backtracking
- [Backtracking](#backtracking)
  - [Introduction](#introduction)
    - [Decision Tree](#decision-tree)
    - [Applications of Backtracking](#applications-of-backtracking)
  - [Example.1 Subset](#example1-subset)
    - [Solution](#solution)
    - [Complexity](#complexity)
  - [Example.2 Subset II](#example2-subset-ii)
    - [Solution](#solution-1)
  - [Example.3 Combination Sum](#example3-combination-sum)
    - [Solution](#solution-2)
  - [Example.4 Combination Sum II](#example4-combination-sum-ii)
    - [Solution](#solution-3)
  - [Example.5 Daily Temperature](#example5-daily-temperature)
    - [Solution](#solution-4)
  - [Example.6 Car Fleet](#example6-car-fleet)
    - [Solution](#solution-5)
  - [Example.7 Largest Rectangle In Histogram](#example7-largest-rectangle-in-histogram)
    - [Solution](#solution-6)

### Introduction
Backtracking is a algorithm technique that searches all possible solution in a incremental and DFS recursive fashion. If a specific path in the search space fails we can roll back to previous states and try a different decision.  
Backtracking can be efficient if we prune redundent branches of the search space.  
#### Decision Tree
An important feature for identifying and implementing backtracking is the problem's decision tree.  
#### Applications of Backtracking
1. Combination
    Select the **elements** from a collection, not taking order into consideration. The result of combination is subsets. A substring/subarray is a subset with constraints about contiguity.  
2. Permutation
    Arrange **all elements** of a collection into some ordered sequence.  
3. Large Search Space
    N-queen, graph coloring, etc. The questions with large search space and pruning is faster than exhaustive brute force.  
### Example.1 Subset
> [Leetcode: 78. Subsets](https://leetcode.com/problems/subsets/)  

Given an integer array `nums` of unique elements, return all possible subsets (the power set).  
> A power set is a set of all subsets including empty set and the original set itself.  
> The number of elements in the power set equal $2^{\text{|set|}}$  

#### Solution
The subsets are related to combination.    
Decision Tree for find all subsets of `nums = [1,2,3]`. For each element in the sub tree we either include it or exclude it.  
```
                           []
  1                    /         \
                 [1]                []
  2             /    \              /   \
           [1,2]       [1]       [2]      []
  3         /  \       /  \      /  \     / \
      [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] [0]
```
Use `tmp` to construct the subset and use `rst` to record all the possible subsets.  
Note that since the work continues with `tmp`, we will make a deep copy of `tmp` when appending it to `rst` instead of using its reference.  
```python
def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    rst = []
    tmp = []
    def dfs(idx):
        if idx == len(nums):
            rst.append(tmp[:])
            return
        tmp.append(nums[idx])
        dfs(idx+1)
        tmp.pop()
        dfs(idx+1)
    dfs(0)
    return rst
```
#### Complexity
We can get the time and space complexity of our backtracking solution by analyzing its decision tree. The height of the decision tree corresponds to the recursion stack depth, which is `len(nums) = O(n)`.  
The total number of nodes corresponds to the number of recursion function calls. Therefore the time complexity is $O(2^{n+1}-1) = O(2^n)$. 

### Example.2 Subset II
> [Leetcode: 90. Subsets II](https://leetcode.com/problems/subsets-ii/)  

Based on example.1, given an integer array `nums` which may contain duplicates, return all possible subsets (the power set).  
The solution set must not contain duplicate subsets.  
#### Solution
Intuitively we can use a set to store all the subsets to avoid duplicates, this will pass the leetcode with no problem. To avoid the same subsets with different orders, we perform dfs backtracking on a sorted input list.  
Another way is to eliminate duplicates is skipping certain branches on the decision tree.  
For example with input `nums = [1,2,2]`  
```
                           []
  1                    /         \
                  [1]                []
  2             /    \              /   \
           [1,2]       [1]       [2]      []
  2        /   x       /  \      /  x     / \
      [1,2,2] [1,2] [1,2] [1] [2,2] [2] [2] [0]
```
For skip the right decision tree for the duplicated elements, only search the right decision tree of the last of the same kind. I don't quite understand how this works but here's the code.   
```python
    def dfs(idx):
        if idx == len(nums):
            rst.append(tmp[:])
            return
        tmp.append(nums[idx])
        dfs(idx+1)
        while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
            idx += 1
        tmp.pop()
        dfs(idx+1)
```

### Example.3 Combination Sum
> [Leetcode 39. Combination Sum](https://leetcode.com/problems/combination-sum/)  

Given an array `candidates` with **distinct** elements and a integer `target`, return a full list of all unique combinations of the array that sum to to `target`. Each number in `candidates` may be chosen for unlimited time.  
#### Solution
A combination problem but each element can be chosen multiple times.  
On the left branch (selected) of the decision tree, we select the same element until the sum exceeds the `target`.  
Do the same operation as usual on the right branch (not selected).  
```python
def dfs(idx):
    if idx == len(candidates) or sum(tmp) >= target:
        if sum(tmp) == target:
            rst.append(tmp[:])
        return
    tmp.append(candidates[idx])
    dfs(idx)
    tmp.pop()
    dfs(idx+1)
```

### Example.4 Combination Sum II
> [Leetcode 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)  

Given an array `candidates` which may contain duplicates and a integer `target`, return a full list of all unique combinations of the array that sum to to `target`. Each number in `candidates` may be chosen for at most **one time**. The solution set must not contain duplicate combinations.
#### Solution
This question is based on Subset II in which we also need to deal with duplicates. 
If sum of `tmp` is >= `target` we return from dfs, otherwise its identical with example.2

### Example.5 Daily Temperature
> [Leetcode 739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the **number of days** you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.  

#### Solution
Monotonically decreasing stack & store extra information in stack.  
1. Initiate an array of the same size with 0s, and an empty stack
2. Iterater through array of temperatures:  
- If temperature lower than stack top, push temperature and index to stack
- If and while temperature, pop top and calculate the number of days = current idx - poped idx, write result to result array 
 
### Example.6 Car Fleet
> [Leetcode 853. Car Fleet](https://leetcode.com/problems/car-fleet/)  

There are ``n`` cars going to the same destination along a one-lane road. The destination is ``target`` miles away.

You are given two integer array ``position`` and ``speed``, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

See full problem description via the link.

Return the **number of car fleets** that will arrive at the destination.
#### Solution
Monotonic stack.  
1. Sort the car position and speed according to position.
> Use zip() function to create truple of iterables:  
> zip(position, speed) -> [(p0, s0), (p1, s1), ..., (pn-1, sn-1)]  

2. Calculate the time needed for each car to reach destination, put in a ``time`` array
> Cars that reach destination in shorter time will catch up and form fleet with slower cars ahead of them.  

3. Initiate a monotonically decreasing stack
4. Iterate through ``time`` array, pop until stack top larger than element, then push element to stack
5. Return the number of element in the stack, which equals to the number of car fleets

### Example.7 Largest Rectangle In Histogram
> [Leetcode 84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)  

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#### Solution
Monotonically increasing stack + extra information to store the width of current height.  
The rectangle of given height can extend to the right, only when right elements are higher.  
Initialize a monotonically increasing stack with width as extra data field.  
Iterate through the array of heights  
- Push to stack when stack empty or height greater equal to stack top
- Pop from stack when height lower than stack top, keep track of cumulative width, calculate area
