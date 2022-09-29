## Binary Search
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
