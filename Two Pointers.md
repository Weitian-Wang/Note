## Two Pointers
- [Two Pointers](#two-pointers)
  - [Introduction](#introduction)
  - [Example 1. Valid Palindrome](#example-1-valid-palindrome)
    - [Solution](#solution)
  - [Example 2. Two Sum II - Input Array is Sorted](#example-2-two-sum-ii---input-array-is-sorted)
    - [Solution](#solution-1)
    - [Complexity](#complexity)
  - [Example 3. 3Sum](#example-3-3sum)
    - [Solution](#solution-2)
    - [Implementation Details](#implementation-details)
    - [Complexity](#complexity-1)
  - [Example 4. Container With Most Water](#example-4-container-with-most-water)
    - [Solution](#solution-3)
  - [Example 5. Trapping Rain Water](#example-5-trapping-rain-water)
    - [Solution](#solution-4)
      - [Solution 1](#solution-1)
      - [Solution 2](#solution-2)
    - [Complexity](#complexity-2)


### Introduction
Two pointers is a technique for searching pairs. Just like sliding window technique, we can usually use two pointers method to get rid of naive nesting for-loops.
### Example 1. Valid Palindrome
> [Leetcode: 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

A phrase is a palindrome if reads the same forward and backward. Ignore cases and non-alphanumeric characters.
#### Solution
By the definition of palindrome we need to compare the string with its backward. Use one pointer to point at the start and one at the end, compare and move towards center until converge.  
> Use built-in str.isalnum method to check if string contains only alphanumeric characters.  

### Example 2. Two Sum II - Input Array is Sorted
> [Leetcode: 167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  

Given a **1-indexed** array of integers `numbers`, which is also **sorted** in non-decreasing order. Find two items that sum up to a specific `target`. And return their index `[ index1, index2 ]` where `1 <= index1 < index2 <= number.length`. One unique solution is guaranteed for every test case.

#### Solution
We can use the map method in the first Two Sum question, which runs at $O(n)$ time with $O(n)$ extra space.  
Since we are now searching for a pair of elements in a sorted array, we can use the two pointer method.  
1. Initialize one pointer `left` at the start of the array, which points at the minimum element in this non-decreasing array
2. Initialize another pointer `right` at the end of the array, which points at the maximum element
3. If sum of elements pointed by the two pointers = target, return index in a list
4. If sum < target, move the `left` pointer towards the end to get a larger number
5. If sum > target, move the `right` pointer towards the start to get a smaller number
#### Complexity
In the worst case this solution scans through almost all the elements in the array, which makes the time complexity $O(n)$. Although the time complexity is comparable to the dictionary solution, two pointer method only requires two constant extra space.  

### Example 3. 3Sum
> [Leetcode: 15. 3Sum](https://leetcode.com/problems/3sum/description/)  

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` which that `i, j, k` are all different indices and three numbers sum up to `0`.  

#### Solution
To find three elements with brute force we need triple nested for-loops. Since we did Two Sum and Two Sum II ealier, we now have two $O(n)$ methods of finding two elements that sum up to a specific target at our pocket.  
Iterate throught the first element `numbers[i]` of the triplets, then reduce the question into a Two Sum problem with `-numbers[i]` as target.  
#### Implementation Details
The problem with dictionary method is duplicated triplets.  
For instance we can get `[-1, 0, 1]` and `[0, 1, -1]`, which is tricky to get rid of as they are treated as different lists by Python.    
```
nums = [-1,0,1,2,-1,-4]
```  
Duplicates are inherently solved if we use two pointers with sorted `nums` array, all the triplets we yield in the process are in the ascending order. If we get two `[-1, 0, 1]` triplets we can simply remove the duplicates with a set.

> List is **NOT** hashable in Python, add them as tuples into the set.  

```
Case 1
nums = [-4,-1,-1,0,1,2]
            ▲  ▲   ▲

Case 2
nums = [-4,-1,-1,0,1,2]
               ▲ ▲ ▲
```
Also as the solution is not unique in this question, we should search until two pointer converge.
```
nums = [-4,0,2,2,4]
         ▲ ▲     ▲
         i j     k

nums = [-4,0,2,2,4]
         ▲   ▲ ▲
         i   j k
```
#### Complexity
If we use two pointer method, which requires a sorted array, the overall $O(n^2)$ complexity will overshadow the $O(n\log n)$ complexity from sorting the array. 

### Example 4. Container With Most Water
> [Leetcode: 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  

Given an integer array `height` of length `n` representing `n` vertical lines of height `height[idx]`. Find two lines that together with x-axis form a container, such that the container can hold the most amount of water.  

#### Solution
"The max water height of a container is determined by the shorter line" - Sun Tzu  
Another factor of the amount of water is the width of the container, which translates to the differential of indices of the selected two lines.  
A $O(n^2)$ brute force solution would be searching through every possible combination of lines.  
1. Initialize two pointers at the start `i` and the end `j` of the array.
2. Calculate the container size = `min(height[i], height[j]) * (j - i)`
3. If `height[i]` < or <= `height[j]` move i forward
4. If `height[i]` >= or > `height[j]` move j backward

### Example 5. Trapping Rain Water
> [Leetcode: 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)  

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water can be trapped after rain.  

#### Solution
The hardest part is to figure out how much water can be trapped in each position. If the volume is negative, no water can be trapped in that position.  
$$
\text{Water Volume} = min(max_{left} , max_{right}) - \text{Current Bar Height}
$$
We can break the problem down to find the max bar height on the left and right sides for each position.  
##### Solution 1
Do a linear scan and use an array to track the max value on the left side of each position.  
Do a reverse scan and use an array to track the max value on the right side of each position.  
Use a third traverse to calculate water at each position and total.  
##### Solution 2
We are looking for the smaller one of left maximum and right maximum.  
Each time advance the side that has smaller max value.  
> If max value on one side is smaller than the temporary max on the other side, its definitely smaller than the actual maximum.  
> Conversely, on the side with larger temporary maximum, we are not sure if there is a even larger value on the other side that is dominant.  
#### Complexity
The naive solution requires find left max, right max for each position, which is $O(n^2)$.  
For solution 1, we need 3 linear iteration $O(n)$ and two extra size-n array $O(n)$.  
The time complexity of solution 2 is $O(n)$ time, with only one iteration for each item.  

