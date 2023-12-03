## Stack
- [Stack](#stack)
  - [Introduction](#introduction)
    - [Characteristics of Heap](#characteristics-of-heap)
    - [Applications of Stack](#applications-of-stack)
  - [Example.1 Kth Largest Element in a Stream](#example1-kth-largest-element-in-a-stream)
    - [Solution](#solution)
    - [Complexity](#complexity)
  - [Example.2 Last Stone Weight](#example2-last-stone-weight)
    - [Solution](#solution-1)
    - [Complexity](#complexity-1)
  - [Example. 3 K Closest Points to Origin](#example-3-k-closest-points-to-origin)
    - [Solution](#solution-2)
    - [Complexity](#complexity-2)
  - [Example 4. Kth Largest Element in an Array](#example-4-kth-largest-element-in-an-array)
    - [Solution](#solution-3)
    - [Complexity](#complexity-3)
  - [Example 5. Task Scheduler](#example-5-task-scheduler)
    - [Solution](#solution-4)
    - [Complexity](#complexity-4)
  - [Example 6. Design Twitter](#example-6-design-twitter)
    - [Solution](#solution-5)
    - [Complexity](#complexity-5)
  - [Example 7. Find Median from Data Stream](#example-7-find-median-from-data-stream)
    - [Solution](#solution-6)
    - [Complexity](#complexity-6)

### Introduction
#### Characteristics of Heap
The addition and removal of elements take place at stack top. The principle by which the stack is ordered is called last-in-first-out (LIFO).  
Native Python list data type can be used as a stack.  
```python
# end of stack/highest index as stack top 
stack = []
# push at top
stack.append(1)
# pop at top
val = stack.pop()
```
#### Applications of Stack
1. Exploit LIFO/FILO property, can be used for backtracking
2. Evaluate expressions (e.g reverse polish notation)
3. Muliple stack, store additional data
4. Monotonic (increasing or decreasing) stack
5. Mixture of 1-4


### Example.1 Kth Largest Element in a Stream
> [Leetcode: 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)   

Design a class to find the $k^{th}$ largest element in a stream. Note that it is the $k^{th}$ largest element in the sorted order, not the $k^{th}$ distinct element.

#### Solution
The smallest number among the $k$ largest numbers is the $k^{th}$ largest element. Initialize a min heap of size $k$. Everytime a new element is added, compare it with the smallest number in the heap.  
1. if number larger than heap top, pop heap top and push new number
2. if smaller, discard new number

#### Complexity
Worst case time complexity $O(n\log n)$.

### Example.2 Last Stone Weight
> [Leetcode: 1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)  

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights $x$ and $y$ with $x <= y$. The result of this smash is:

- If $x == y$, both stones are destroyed
- If $x != y$, the stone of weight $x$ is destroyed, and the stone of weight $y$ has new weight $y - x$.
At the end of the game, there is at most one stone left.  
Return the weight of the last remaining stone. If there are no stones left, return 0.  

#### Solution
Use a max heap for all the stones. Pop the largest number and the second largest number from the heap and push the new weight back to the heap.    
The heap from Python `heapq` is min heap. To implement a max heap with min heap, store the negative of the value. 

#### Complexity
Time complexity for `heapify` is $O(\log n)$. In each step, we eliminate one weight, until there is only one weight left. The process is repeated $n$ times. The overall time complexity $O(n)$.

### Example. 3 K Closest Points to Origin
> [Leetcode 973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)  

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

#### Solution
Use a max heap of size k to track the k smallest distances. If the new distance is smaller than heap top, pop heap top and push new value.  

Use tuple as heap elements. [To compare tuples](https://docs.python.org/3/reference/expressions.html#value-comparisons).

#### Complexity
Like the Kth Largest Element problem, the worst case time complexity is $O(n\log n)$.

### Example 4. Kth Largest Element in an Array
> [Leetcode 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)  

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.  
Note that it is the kth largest element in the sorted order, not the kth distinct element.  
Solve this problem without sorting.  

#### Solution
Use a min heap of size $k$, push each item into the heap if the number larger than heap top.  

#### Complexity
Time complexity for heap push and pop operations is $O(\log k)$. Overall time complexity $O(n\log k)$.  

### Example 5. Task Scheduler
> [Leetcode 621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)  

Given a character array `tasks`, representing the tasks a CPU needs to do, where each character represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.  

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.  

Return the least number of units of times that CPU will take to finish all tasks.  

#### Solution
Intuition of solving this problem is that when scheduling tasks we should prioritize the most frequent task. Therefore a max heap should be used.   

To make the solution more organized and intuitive, use a queue to store the tasks in cool down and dequeue them after the current time passes their cool down time.  

1. Simulate the process by advance the time by one unit at a time.  

If current time exceeds the cool down time of task at the front of the queue, dequeue that task and push back to max heap.  

Choose the task at heap top, enqueue this task along with it's cool down time.  

If there's no task in heap, which mean all tasks are in cool down, CPU runs idle at this time frame.   

Repeat until exhaust all the tasks in both heap and queue.  
#### Complexity
There are 26 characters at most, therefore create, push, and pop of the max heap have same time complexity of $O(\log 26)$. The overall time complexity is $O(n)$ where $n$ is the total number of tasks as each task has to be processed once.  

### Example 6. Design Twitter
> [Leetcode: 355. Design Twitter](https://leetcode.com/problems/design-twitter/)

Design a simplified version of Twitter where user can post, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.  

#### Solution
Use a dictionary to record user's set of followee.  
Either use a list to store all tweets in chronological order, or use heap to find the top 10 most recent tweets on request.  
#### Complexity


### Example 7. Find Median from Data Stream
#### Solution
#### Complexity