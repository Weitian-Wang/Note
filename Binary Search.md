## Binary Search
- [Binary Search](#binary-search)
  - [Basic Version](#basic-version)
    - [Solution](#solution)
    - [Execution Details](#execution-details)
    - [Complexity](#complexity)
  - [Example.1 First Bad Version](#example1-first-bad-version)
    - [Solution](#solution-1)
    - [Variations](#variations)
  - [Example.2 Search a 2D Matrix](#example2-search-a-2d-matrix)
    - [Solution](#solution-2)
  - [Example.3 Find Minimum In Rotated Sorted Array](#example3-find-minimum-in-rotated-sorted-array)
    - [Solution](#solution-3)
  - [Example.4 Rotated Sorted Array I](#example4-rotated-sorted-array-i)
    - [Solution](#solution-4)
  - [Example.5 Rotated Sorted Array II](#example5-rotated-sorted-array-ii)
    - [Solution](#solution-5)
  - [Example.6 Median of Two Sorted Arrays](#example6-median-of-two-sorted-arrays)
    - [Solution](#solution-6)
    - [Execution Details](#execution-details-1)

### Basic Version
> [Leetcode: 704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an **sorted** (ascending) array of integer `nums` and a integer `target`, find the index of the target, or return -1 if non-existent.
#### Solution
1. Initial state:
- start / left / lo = 0
- end / right / hi = len(nums) **- 1**
    > Note: In a 0-indexed array, the last index of the array is length - 1.
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
> For the sake of consistency, this part only shows one version of implementation I usually stick with.  

  - Loop condition: `while start <= end`, exit the loop when `start` and `end` crossed over
  - Must check `if nums[mid] == target` before shrinking boundaries
  - Shrink end: `end = mid - 1`
  - Shrink start: `start = mid + 1`
  - After loop: if exit the loop without finding any `nums[mid] == target`, target not in array

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

### Example.1 First Bad Version
> [Leetcode: 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)  
> One variation is [Leetcode: 875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

Instead of sorted list, we have `n` versions `[1, 2, 3, ..., n]`, objective is to find the first bad one which all following ones are bad. 
```
Ver.No   1  2  3  4  ...  n-1  n
Status   ✓  ✓  ✕  ✕  ...   ✕   ✕
               ▲
              this
```
> Note that this is equivalent to search in a 1-indexed array.  

#### Solution
We can use the binary search to search the inorder predecessor of a given key.  
1. Initialize `start = 1` and `end = n`
2. `mid` = `(start+end)//2`
3. If `isBadVersion(mid)`, search left half, `end = m - 1`
4. Else, search right half `start = m + 1` 

Once `start` and `end` cross over each other, `end` will be pointing at the last good version. Add one to `end` we will get the first bad version.
#### Variations
[Leetcode: 875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)  
[Leetcode: 1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)  

### Example.2 Search a 2D Matrix
> [Leetcode: 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)  

Given an `m x n` integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

```
[ 1   3   5   7  ]
[ 10  11  16  20 ]
[ 23  30  34  60 ]
```

#### Solution 
For a $O(m\times n)$ solution we will have to iterate through all elements in the matrix.  
For a $O(\log (n*m))$ solution we can use binary search by treating the matrix as a 1D array. We have to convert `row` and `column` indices to the `offset`.   
For a $O(\log (n+m))$ solution, first binary search the row, then search `target` in that row.  

To search the `row` the `target` may be in, we need to find the row with the maximum first element that is smaller than `target`. Search with the same implementation used in the [Basic Version](#basic-version), `end` will be pointing at the predecessor.  


### Example.3 Find Minimum In Rotated Sorted Array
> [Leetcode: 153. Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array `nums = [0,1,2,4,5,6,7]` might become: 
- `nums = [0,1,2,4,5,6,7]`
- `nums = [5,6,7,0,1,2,4]`

Find the minimum value in the rotated sorted array.  

#### Solution
- Use a global variable `result` to track the minimum value.  
- Initialize `start, end = 0, len(nums) - 1`
- `mid = (start+end)//2`, one exception minimum may occur at `mid`, so `result = min(result, nums[mid])`
- If right partition sorted, search in left half, `end = mid - 1`
- If left partition sorted, search in right half, `start = mid + 1`
The minimum value resides where the order of array inverts. That is to say minimum value is in the unsorted part of the array with one exception at the `mid`.  
```
index  0  1  2  3  4  5  6
nums   5  6  7  0  1  2  4
       ▲        ▲        ▲
       │        │        │                   
      start     mid      end  
``` 

### Example.4 Rotated Sorted Array I
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

### Example.5 Rotated Sorted Array II
> [Leetcode: 81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

Based on question [Example.4](#example4-rotated-sorted-array-i), but the elements can be the same (**not** necessarily **distinct**).
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

### Example.6 Median of Two Sorted Arrays
> [Leetcode: 5. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)  

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be $O(\log (m+n))$.


#### Solution
To find the median, we need to partition arrays `nums1` and `nums2` to two equal partitions respectively, so that all numbers in the left half is smaller than all numbers in the right half.  

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # partition the short array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, len1 - 1
        while -1<=j:
            # partition point m1, indicates the right most element in the right partition
            m1 = (i+j)//2
            # right partition have one more element
            m2 = (len1 + len2)//2 - m1 - 2
            l1 = nums1[m1] if m1 >= 0 else float('-inf')
            l2 = nums2[m2] if m2 >= 0 else float('-inf')
            r1 = nums1[m1+1] if m1 + 1 < len1 else float('inf')
            r2 = nums2[m2+1] if m2 + 1 < len2 else float('inf')
            if l1 <= r2 and l2 <= r1:
                break
            if l1 > r2:
                j = m1 - 1
            else:
                i = m1 + 1
        return min(r1, r2) if (len1+len2)%2 else (max(l1, l2)+min(r1, r2))/2.0
```

#### Execution Details
We make sure we do binary search in the shorter array, so that the `m2` will be in boundary of the second array.  
We can take at least 0 items from the shorter array, which means index `m1` can be -1, assign `float('-inf')` for comparison.  
We can take at most all the items from the shorter array, which means index `m1` can be `len(nums1) - 1`.
