# Sliding Window
- [Sliding Window](#sliding-window)
  - [Introduction](#introduction)
    - [Sliding Window vs Two Pointers](#sliding-window-vs-two-pointers)
  - [Example 1. Best Time to Buy and Sell Stock](#example-1-best-time-to-buy-and-sell-stock)
    - [Solution](#solution)
    - [Complexity](#complexity)
  - [Example 2. Longest Substring Without Repeating Characters](#example-2-longest-substring-without-repeating-characters)
    - [Solution](#solution-1)
    - [Complexity](#complexity-1)
  - [Example 3. Longest Repeating Character Replacement](#example-3-longest-repeating-character-replacement)
    - [Solution](#solution-2)
      - [Condition Check](#condition-check)
      - [Iteration Method](#iteration-method)
      - [Implementation Details](#implementation-details)
    - [Complexity](#complexity-2)
  - [Example 4. Permutation in String](#example-4-permutation-in-string)
    - [Solution](#solution-3)
      - [Condition Check](#condition-check-1)
      - [Iteration Method](#iteration-method-1)
      - [Implementation Details](#implementation-details-1)
    - [Complexity](#complexity-3)
  - [Example 5. Minimum Window Substring](#example-5-minimum-window-substring)
    - [Solution](#solution-4)
      - [Condition Check](#condition-check-2)
      - [Iteration](#iteration)
      - [Implementation Details](#implementation-details-2)
    - [Complexity](#complexity-4)
  - [Example 6. Sliding Window Maximum](#example-6-sliding-window-maximum)
    - [Solution](#solution-5)
      - [Analysis](#analysis)
      - [Text Description of Pseudocode](#text-description-of-pseudocode)
      - [Execution Details](#execution-details)
    - [Complexity](#complexity-5)

## Introduction
We can use sliding window technique to reduce time complexity for some subarray problems that require nesting for-loops as naive solutions.
### Sliding Window vs Two Pointers
Two pointers is implemented with two pointers. We usually compare the **two values** pointed by the two pointers.  
Sliding window is implemented with a window start pointer and a window size variable. We usually care about **all the elements** in current window frame.
## Example 1. Best Time to Buy and Sell Stock
> [Leetcode: 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)    

Given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day. Maximize the profit by choosing a single day to buy, and a future day to sell.

### Solution
A naive $O(n^2)$ solution is using nesting for-loops. For each element in `price` iterate through all elements behind current element.  
A improved solution can be achieve with $O(n)$ linear scans and additional $O(n)$ space. In the first iteration find the min price so far, store it in the additional array. In the second iteration find the maximum difference between current value and previous min price.  
The optimal solution is using a sliding window or two pointers.  
1. Initialize `left` = `right` = `0`
2. While the element at index `left` <= `price[right]`, increment right
3. If `price[left]` > `price[right]`, we find a new local minimal at `right`, let `left` = `right` 
4. Repeat until `right` hits the end of the `prices` array
### Complexity
We optimized the solution from $O(n^2)$ to $O(n)$.  
The two iteration method costs $O(n)$ time complexity and $O(n)$ special complexity with the additional array.  
The sliding window / two pointer method doesn't need extra memory, and the time complexity is $O(n)$.  

## Example 2. Longest Substring Without Repeating Characters
> [Leetcode: 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the longest substring without repeating character.  

### Solution
To check if the substring has repeating characters. We can use a hash table to check if given character has been seen before. In Python we can use a `set`.  
A naive solution would be going through all possible substrings, which costs $O(n^2)$ with nesting for-loops. Find the longest amongst those without repeating characters is another $O(n)$ complexity operation within the double nested for-loops. Overall complexity would be $O(n^3)$.  
With the sliding window technique.
1. Initialize a set `seen` that keeps track of characters in current window
2. Initialize the `i` and `j` = 0, where `i` is the left bound and `j` is the right bound of the current window
3. Expand window if current substring is having non-repeating characters. Add next character at the right to the window.
4. Shrink window if current substring has repeating characters. Evict the left most char from window.
### Complexity
For the optimal solution, we use $O(n)$ extra space for the `set` and the time complexity is `O(n)`.

## Example 3. Longest Repeating Character Replacement
> [Leetcode: 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)  

Given a string `s` and an integer `k`. Perform change of any characters for at most `k` times. Find the length of longest substring with the **same** character with the above operation.

### Solution
#### Condition Check
To check if a substring can have the same character after `k` changes. Assume the character with most number of occurance is the target character we'd like to change other characters to. Use a dictionary or counter to track the number of occurance. When the window size <= k + max number occurance, we can make the substring homogeneous within `k` changes.  
#### Iteration Method
Naively we can screen every possible substring.  
For an optimized solution, we can use the sliding window method. We expand the window rightward if current window passes the condition check, elsewise shrink the window and evict leftmost character from the dictionary counter. 
#### Implementation Details
As we are pointing right window boundary `j` to the next position, the last window is not checked in the loop. Check the last window then return final result.
```python
if max(counter.values())+k >= j-i:
    rst = max(j-i, rst)
```
### Complexity
For the condition check, we need a dictionary of size $O(n)$ worst case. For each window change, we find the maximum occurance which requires us to iterate through all dictionary values, which costs $O(n)$ time.  
To traverse the string with sliding window methods takes `$O(n)` time.  
Therefore the overall time complexity $O(n^2)$ and space complexity $O(n)$.

## Example 4. Permutation in String
> [Leetcode: 567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)  

Given two strings `s1` and `s2`, check if any of `s1`'s permutation is the subtring of `s2`.

### Solution
#### Condition Check
For one string to be the permutation of another string, they need to have the same number of each character, which can be achieved by comparing two counter dictionaries.
#### Iteration Method
A brute force method would be going through all substrings of `s2` that has the same length of `s1`. We will have to rebuild the dictionary each time.  
With sliding window technique, we can add one character and kick out one character from counter at each iteration.  
#### Implementation Details
How to Initialize a Fixed Size Window  
1. Use a while loop before the loop for advancing the window
2. Or we can combine them in to one while loop. If window is smaller than target size, expand the window, else move the window forward  
> By using the second method, the corner case where `len(s1)` is greater than `len(s2)` is automatically solved.


Edge Case Handling  
In my implementation I'd usually point `j` to the **next position**. Therefore the last window position is not checked within the while loop.  
```python
while j < len(s2):
    ...
    self.isPermutation(d1, d2)
    # add s2[j] to dict
    # remove s2[i] from dict
    # j += 1
    # i += 1
return self.isPermutation(d1, d2)
```

### Complexity
Let `m`, `n` be the length of `s1` and `s2` respectively. The extra space for storing the counter is $O(26)$.  
The time complexity of dictionary comparison is $O(26)$. Assuming in the worst case `n` is large enough that it's dominating `m`, the number of window movements would be close to `n`. Therefore the overall worst case time complexity $O(26n)=O(n)$.  


## Example 5. Minimum Window Substring
> [Leetcode: 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  

Given two strings `s` and `t` of lenght `m` and `n` respectively, return the minimum window substring of `s` that includes every character in `t` including duplicates. If there is no such substring return "".

### Solution
#### Condition Check
Check if substring of `s` has every character of `t` in it. For each character in `t`, the substring must have more of that same character.  
#### Iteration
1. Expand the window if current substring doesn't satify the condition
2. Shrink the window if current substring satifies the condition, to find the minimum
#### Implementation Details
1. Result is the shorter one between qualified substring and itself. But initially `result = ""`, update it to the first qualified substring.
2. The right boundary pointer j points at the next character, we need to handle the final window.  

Most elegant way instead of using another while-loop outside.
```python
while j < len(s):
    if substring not valid:
        expand window
        add s[j] to counter
        j += 1
    # takes care of the last window if its valid
    while substring valid:
        shrink
```
### Complexity
The extra dictionary space $O(26*2)$ as the strings consist of uppercase and lowercase letters. The comparison between the two dict takes $O(26*2)$ which is constant worst-case time. Iterate through the longer string takes $O(n)$ time.

## Example 6. Sliding Window Maximum
> [Leetcode: 239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)  

Given an array integers `nums`, there is a sliding window of size `k` which is moving from left of the array to the right. Each time the sliding window moves right by one position.  Return the max in sliding window in each step.  

```
Window position                Max
-------------------------     -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Return: [3, 3, 5, 5, 6, 7]
```
### Solution
#### Analysis
Naively we have a $O(n^2)$ solution by going through each item in each sliding window.  
For a better solution, we can use the sliding window method, add and remove from the window in each iteration. We need a data structure for adding elements into it and keep track of the maximum. A heap might be tempting, but it's not good at remove a given item.  
We can use a monotonically decreasing stack to keep track of the maximum value.  
We'd also like to remove item from the front of the stack.  
Therefore a deque (double-ended queue) which combines the functionalities of both queue and stack.  
#### Text Description of Pseudocode
1. Initialize a deque
2. Push first `k` items to the deque in the monotonically decreasing fashion
3. Repeat
    - Add the first deque element to result list
    - If left-most item is the first deque element, remove it
    - Add the next item to the deque in the monitoncially decreasing fashion
#### Execution Details
One edge case if current window is `... [3 3 1] 2 ...`, we may accidentally remove the max in the next window postion. If an item is equal to the deque stack top we still have to push it into the deque. This way we create a weakly decreasing deque.
### Complexity
The space complexity is $O(k)$ for the deque, which in the worst-case is $O(n)$.  
We go through each item twice, the first time pushing them into the stack and the second time popping them out. The time complexity is $O(n)$.
