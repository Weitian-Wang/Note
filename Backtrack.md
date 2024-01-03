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
	- [Example.5 Permutations](#example5-permutations)
		- [Solution](#solution-4)
		- [Complexity](#complexity-1)
	- [Example 6.Word Search](#example-6word-search)
		- [Solution](#solution-5)
	- [Example 7.Palindrome Partitioning](#example-7palindrome-partitioning)
		- [Solution](#solution-6)
		- [Complexity](#complexity-2)
	- [Example 8. Letter Combination of a Phone Number](#example-8-letter-combination-of-a-phone-number)
		- [Solution](#solution-7)
		- [Complexity](#complexity-3)
	- [Example 9. N-Queens](#example-9-n-queens)
		- [Solution](#solution-8)
			- [To check if a placement at position (i, j) is valid](#to-check-if-a-placement-at-position-i-j-is-valid)
			- [Decision Tree](#decision-tree-1)
			- [Base Condition and Initial Status](#base-condition-and-initial-status)
			- [Code](#code)
		- [Complexity](#complexity-4)

### Introduction
Backtracking is a algorithm technique that searches all possible solution in a incremental and DFS recursive fashion. If a specific path in the search space fails we can roll back to previous states and try a different decision.  
Backtracking can be efficient if we prune redundant branches of the search space.  
#### Decision Tree
An important feature for identifying and implementing backtracking is the problem's decision tree.  
Identify what are the options at each step, try out different paths of the decision tree.  
After traversing one possible path of the decision tree, usually in a DFS fashion, revert(hence backtrack) everything to previous status and try search another path.  
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

### Example.5 Permutations
> [Leetcode 46. Permutations](https://leetcode.com/problems/permutations/description/)  

Given an array of unique numbers `num`, return all the possible permutations.

#### Solution
In the combination problem the decision tree is binary. In each decision step we either take current element and move on or we don't.  
For permutations, the decision tree is k-nary, where each of the remaining element in the list could be selected.  
Loop through all elements in the `num`, add it to the temporary result, and recurse with the list `num` without the selected element.  
#### Complexity
The number of permutation is the time complexity $O(n!)$.  
The depth of recursion stack is $O(n)$, which corresponds to the space complexity.  

### Example 6.Word Search
> [Leetcode 79. Word Search](https://leetcode.com/problems/word-search/description/)  

Given an `m x n` grid of characters `board` and a string `word`, return `True` if `word` exists in the `board`.  

#### Solution 
Decision at each step, take current letter or not?  
To avoid timeout, count all letters in the grid and check if there's enough letter to form the word.  
For each staring position (i, j), perform a depth first search to see if the `word` can be constructed starting from the letter at position (i, j).  
Use a set to track the visited position in each DFS, and remove position from set after performing DFS.

### Example 7.Palindrome Partitioning
> [Leetcode 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)  

Given a string `s`, partition it so that every substring of the partitioning is a palindrome. Return all such partitioning of `s`.

#### Solution
When partitioning the input the string, we have two choices at each letter of `s`.  
1. Add letter to the existing substring
2. End previous substring and start a new substring with letter

Pruning the decision tree to reduce the number of search paths.  
E.g. If we decide to start another substring and the previous substring is not a palindrome, its the invalid path.  

#### Complexity
The worst case time complexity would be $O(2^{n})$ as we check all possible partitioning of `s`.  
Suppose empty substring is not allowed, there are $n-1$ possible partition points for a string of length $n$. At each point we can either partition or not. Therefore the total number of partitioning is $2^{n-1}$.

### Example 8. Letter Combination of a Phone Number
> [Leetcode 17. Letter Combination of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)  

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.  

#### Solution
Suppose we scanning the input number from left to right. At each digit, we can choose from either 3 or 4 letters the number could represent, and add it to the string we are constructing.  

```python
num_to_letter = {
    '1': 'abc',
    '2': 'edf',
    # ...
    '9': 'wxyz'
}

rst = []
def dfs(idx, curStr):
    if idx == len(digits):
		rst.append(curStr)
		return
	for letter in num_to_letter[digits[idx]]:
		dfs(idx+1, curStr+letter)
```

#### Complexity
As we search through every branch of the decision tree, the time complexity of the DFS algorithm is $O(4^n)$. 4 is the max number of letters a digit could represent, n is the length of `digits`.  

### Example 9. N-Queens
> [Leetcode 51. N-Queens](https://leetcode.com/problems/n-queens/)   

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.  

#### Solution
The solution ignores the problems specific details and covers the general ideas.  
##### To check if a placement at position (i, j) is valid
For each queen already placed at (x, y), check
1. If the two queens are in the same row, i == x
2. If the two queens are in the same column, j == y
3. If the two queens are in the main diagonal, i - j == x - y
```
Matrix of value row - column 
[0, -1, -2, -3]
[1,  0, -1, -2]
[2,  1,  0, -1]
[3,  2,  1,  0]
```
4. If the two queens are in the anti-diagonal, i + j == x + y
```
Matrix of value row + column 
[0, 1, 2, 3]
[1, 2, 3, 4]
[2, 3, 4, 5]
[3, 4, 5, 6]
```
##### Decision Tree
At each fixed row `i`, we can choose to place the queen at column `j`, if position `(i, j)` is valid.  
The decision tree is n-nary, as we have `n` choices at each step.  
1. DFS Part
Then repeat the search process with next row `i+1`.  
2. Backtrack Part
Remove from position `(i, j)` and try out the rest of the column positions `j+1, j+2, ..., n-1`.  

##### Base Condition and Initial Status
Base condition is a condition where the DFS reaches the bottom of recursion. In this case when the row(0 indexed) reaches `n`, which means we've successfully placed all `n` queens in row `0 to n-1`. Add the current placement we worked on to the overall solution.  

Initially there's no placement, the current placement data structure is empty. Start the DFS process from row 0.  

##### Code 
```python
 def solveNQueens(self, n):
   # all valid placement
   sols = []
   # current placement
   placed = []

   def is_valid(i, j):
      for (x, y) in placed:
          if i == x or j == y or i - j == x - y or i + j == x + y:
              return False
      return True

   def dfs(i):
      if i == n:
          sols.append(placed.copy())
          return
      for j in range(n):
          if is_valid(i, j):
              placed.append((i, j))
              dfs(i+1)
              placed.pop()

   dfs(0)
   return sols
```
#### Complexity
There are $n^n$ possible placements therefore the search space is $n^n$.  
> Complexity to be verified  


Using the backtracking method, the algorithm tries `n` positions in the first row. For each position, the algorithm tries at most `n-1` positions in the second row, and so on and so forth.  
The maximum number of time of the recursive function being called is $n!$.  


