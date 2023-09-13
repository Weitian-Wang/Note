## Linked List
- [Linked List](#linked-list)
	- [Introduction](#introduction)
	- [Example.1 Reverse Linked List](#example1-reverse-linked-list)
		- [Solution - Iterative](#solution---iterative)
		- [Complexity - Iterative](#complexity---iterative)
		- [Solution - Recursive](#solution---recursive)
		- [Complexity - Recursive](#complexity---recursive)
	- [Example.2 Merge Two Sorted Lists](#example2-merge-two-sorted-lists)
		- [Solution](#solution)
		- [Complexity](#complexity)
	- [Example.3 Reorder List](#example3-reorder-list)
		- [Solution](#solution-1)
	- [Example 4. Remove Nth Node From End of List](#example-4-remove-nth-node-from-end-of-list)
		- [Solution](#solution-2)
		- [Complexity](#complexity-1)
	- [Example.5 Copy List With Random Pointer](#example5-copy-list-with-random-pointer)
		- [](#)
		- [Complexity](#complexity-2)
	- [Example 6. Linked List Cycle](#example-6-linked-list-cycle)
		- [Solution](#solution-3)
		- [Complexity](#complexity-3)
	- [Example 7. Find the Duplicated Number](#example-7-find-the-duplicated-number)
		- [Solution](#solution-4)
		- [Complexity](#complexity-4)
	- [Example 8. LRU Cache](#example-8-lru-cache)
		- [Solution](#solution-5)
		- [Complexity](#complexity-5)
	- [Example 9. Merge k Sorted Lists](#example-9-merge-k-sorted-lists)
		- [Solution](#solution-6)
		- [Complexity](#complexity-6)
	- [Example 10. Reverse Nodes in k-Group](#example-10-reverse-nodes-in-k-group)
		- [Solution](#solution-7)

### Introduction
Linked list is a data structure where nodes are connected by link. Each node contains a data field and a reference to the next node.  
For the sake of consistency in edge cases (empty linked list) and easier handling of the linked list, I'd like to introduce a dummy node before the head node.  

```
	 ┌─┐  ┌─┐  ┌─┐  ┌─┐  ┌─┐
	 │1├─►│2├─►│3├─►│4├─►│5│
	 └─┘  └─┘  └─┘  └─┘  └─┘

┌─┐  ┌─┐  ┌─┐  ┌─┐  ┌─┐  ┌─┐
│H├─►│1├─►│2├─►│3├─►│4├─►│5│
└─┘  └─┘  └─┘  └─┘  └─┘  └─┘
```

### Example.1 Reverse Linked List
> [Leetcode: 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  

Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Solution - Iterative
Use two pointer `prev` and `cur` to track the previous node and the current node. Set `cur.next` to `prev` and move forward.  
#### Complexity - Iterative
Time complexity $O(n)$, with no extra space $O(1)$.  
#### Solution - Recursive
Repeat the iterative work above at each recursion call, return the last node as new head.  
```python
def reverseList(self, head):
	new_head = head
	while head and head.next:
		# dfs to get the last node
		new_head = self.reverseList(head.next)
		head.next.next = head
		head.next = None
	return new_head
```
#### Complexity - Recursive
Time complexity $O(n)$, recursion stack depth $O(n)$. 

### Example.2 Merge Two Sorted Lists
> [Leetcode: 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)  

You are given the heads of two sorted linked lists `list1` and `list2`, both in non-decreasing order.  

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.  

Return the head of the merged linked list.  
#### Solution
Same principle as merge two sorted list, but we are working on linked list this time. Each time find the smaller value of two candidates, append it to our merged list then move forward. Repeat until one list depletes and extend the other remaining list to result.  
#### Complexity
We merged two linked list in place with no extra memory, space complexity $O(1)$.  
Time complexity $O(m+n)$ as we iterate through each node once, where `m` and `n` are the lengths of two linked list respectively.  
### Example.3 Reorder List
> [Leetcode 143. Reorder List](https://leetcode.com/problems/reorder-list/description/)  

Given the head of a singly linked-list. The list can be represented as:  
```
L0 → L1 → … → Ln - 1 → Ln
```
Reorder the list to be on the following form:  
```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```
You may not modify the values in the list's nodes. Only nodes themselves may be changed.  

Example:  
```
Before Reordering
┌─┐  ┌─┐  ┌─┐  ┌─┐  ┌─┐
│1├─►│2├─►│3├─►│4├─►│5│
└─┘  └─┘  └─┘  └─┘  └─┘

After Reordering
┌─┐  ┌─┐  ┌─┐  ┌─┐  ┌─┐
│1├─►│5├─►│2├─►│4├─►│3│
└─┘  └─┘  └─┘  └─┘  └─┘
```
#### Solution
The reorder can be achieved by doing three steps:
1. Find the middle node of the linked list
2. Reverse the second half of the linked list
3. Merge two linked lists in alternating order

Naively if we'd like to find the middle point of the linked list, we can calculate the length of the linked list in the first pass and find the mid point in the second pass.  
There exists a technique that only requires a single pass: ***fast and slow pointers***.  

Initialize a `slow` and a `fast` pointer both pointing at the extra `handler` node. Each time, the `slow` pointer move one step to the next node, `fast` pointer move two steps forward. Repeat until `fast` reaches the end of the linked list.  

This implementation ensures that the first part of the linked list has more or equal number of nodes than the second part.  

Reverse second half of the linked list with iterative or recursive methods.  

Merge two linked lists in interleaving order.  

### Example 4. Remove Nth Node From End of List
> [Leetcode: 19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Given an `head` of linked list, remove the `n-th` node from the **end** of the list and return its head.  

#### Solution
Few things to mention about this problem.  
Edge cases:  
1. If target node is the 1-th node from the end
2. If target node is the n-th node from the end, where `n` is the length of the list
To write elegant code without explicitly handling edge cases, we use a dummy node in front of the `head` node.  

To find the `n-th` node from the back:  
1. Two pass method, get total length in the first pass, find `length - n` th node in the second pass
2. `n` extra storage method, traverse an store nodes in a list
3. Optimal method, use two pointers, one pointer `n` steps ahead of the other

To delete an node in a linked list:  
1. We need to access the node before the target node

#### Complexity
Worst-case time $O(n)$ for deleting the `1-th` item from the end, we need to iterate through all elements.  
Space complexity $O(1)$ with no extra space.  


### Example.5 Copy List With Random Pointer
> [Leetcode: 138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)  

Given a linked list of length `n`, each node contains an additional random pointer that points to any node in the list or `null`.  

```
Node
┌─────────┐
│ value   │
├─────────┤
│ next    │
├─────────┤
│ random  │
└─────────┘
```

Construct a deep copy of the list.  

#### 
Floyd's slow and fast pointer algorithm.
For each node in the original linked list, create a new node with the same value. Meanwhile use a dictionary to map the old node to the new node.  
In the second iteration, create corresponding links for the random pointers by looking up the dictionary.  

#### Complexity
Time complexity $O(n)$ for iterating through `n` elements twice.  
Space complexity $O(n)$ for the dictionary with `n` items.  

### Example 6. Linked List Cycle
> [Leetcode: 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)  

Given `head` of a linked list, determine if the linked list has a cycle in it.  

#### Solution
Floyd's cycle detection algorithm, fast and slow pointer.  
Initialize two pointers `fast` and `slow` pointing at the head. For each step `slow` pointer moves, move `fast` two steps ahead.  
If `fast` pointer reaches `null`, there is no cycle in given linked list.  
If `fast` pointer and `slow` pointer overlaps at some point of the iteration, cycle detected.  
#### Complexity
Omit the proof time complexity is $O(n)$.  

### Example 7. Find the Duplicated Number
> [Leetcode: 287. Find the Duplicated Number](https://leetcode.com/problems/find-the-duplicate-number/)  

Given an array of integers `nums` containing `n+1` integers where each integer is in range $[1, n]$ inclusive.  
There is **only one** repeated number `num`, return that number.  
Solve this problem **without** modifying the array `nums` and use only **constant** extra space.


#### Solution
Thought process:  
1. Brute force  
	Use double for-loop to check if any element is the same as the current element.  
	Time complexity $O(n^2)$.  
2. Sort
	Sort the array and check if two adjacent elements are duplicates.  
	Time complexity $O(n\log n)$ if use quicksort.
3. Hash
	Use a dictionary to check if element has occured before.  
	Time complexity $O(n)$ but with $n$ extra space.

Convert it to known problem.  
If there is no duplicated elements in the array, each element is going to point to a unique index. We can view this array as a linked list where each element points at the next node.  
However if there is a repeated number in the array, the two identical elements are pointing at the same index. Therefore in this scenario there is a cycle in the linked list.  

Example:  
```
Input: nums = [1,3,4,2,2]
Output: 2
```
```
index 0 1 2 3 4
nums  1 3 4 2 2
linked list visualization
0->1->3->2->4->2
            ▲  │
            └──┘
```
The node before the loop is the duplicated number. Convert this problem to finding the starting point of the loop.  

Solution steps:  
1. Use Floyd's loop detection algo to find the loop.  
2. Initialize a pointer_1 to head, and set pointer_2 at its position in step 1
3. Move pointer_1 and pointer_2 **one step** at a time
4. The overlap point is the start of the loop
   
Proof:  
```
		m				  k
head──►...──►loop_head──►...──►overlap──►...──┐
                 ▲                            │
                 │                            │
                 └────────────────────────────┘
				 			   n
m: the distance of loop head from list head
n: the length of loop
k: the distance of overlap point in Floyd's loop detection algo from loop head
```
$$d_{fast} = 2 \times\ d_{slow}$$
Let $x$ be the number of loops fast pointer traveled  
Let $y$ be the number of loops slow pointer traveled  
$$m+x\times n+k = 2\times(m+y\times n+k)$$
$$\rArr$$
$$(x-2y)n=m+k$$
Which means $m+k$ is a multiple of n.  
Start pointer_1 at head and pointer_2 at overlap and move them forward one step at a time, by the time pointer_one reaches loop_head, pointer_2 also moved $m$ steps and now its $m+k$ steps **away** from loop_head.  
Since $m+k$ is a multiply of $n$ the pointer_2 is also at loop_head.  
#### Complexity
Time complexity $O(n)$ with constant extra space.

### Example 8. LRU Cache
> [Leetcode: 146. LRU Cache](https://leetcode.com/problems/lru-cache/)

Design a data structure that follows the constraints of a Least Recently Used cache.  
#### Solution
Use a queue to track the usage of the keys overtime. Move the key to the front of queue whenever the key is written or accessed. To evict the least recently used key, remove the key at the rear of the queue.  
Implement a queue with doubly linked list and speed up the lookups with a dictionary.  
> Tips: Use one dummy node at front and another dummy node at rear since we are doing operations on both ends. The use of dummy nodes can simplify the handling of edge cases.  

#### Complexity
Read and write operations take constant average time.

### Example 9. Merge k Sorted Lists
> [Leetcode: 23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

Given `lists` of an array of `k` linked lists, each linked list is sorted in ascending order. Merge all linked lists into one sorted linked list and return it.  
#### Solution
A brute force solution would iterate through all lists and merge each list into the result list.  
Time complexity analysis of the brute force algorithm:  
Assuming each linked list have the same number of nodes $m$, and there are a total of $n$ linked lists in `lists`.  
The `m` nodes in the 1st linked list is visited `n` times, and the the `m` nodes in the 2nd linked list is visited `n-1` times, and so forth. And the number of iteration is $\frac{m(n^2+n)}{2}$ which is $O(n^2)$.   

We can use divide and conquer to improve the run time. Merge the two neighboring linked lists each time and eventually getting one result list.  
```
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐     ┌─────┐ ┌─────┐ ┌─────┐
│ l_1 │ │ l_2 │ │ l_3 │ │ l_4 │ ... │l_n-2│ │l_n-1│ │ l_n │
└──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘     └─────┘ └─────┘ └─────┘
   └───┬───┘       └───┬───┘
┌──────┴──────┐ ┌──────┴──────┐             ┌─────────────┐
│  l_1 + l_2  │ │ l_3 + l_4   │ ...         │l_n-1 + l_n  │
└─────┬───────┘ └───────┬─────┘             └─────────────┘
	  └────────┬────────┘
┌──────────────┴──────────────┐
│       l_1 ... l_4           │
└─────────────────────────────┘
```
#### Complexity
At each step of divide and conquer, we make two recursive calls on the subproblems with half input size. The recursive relation can be represented by $f(n) = 2\times f(\frac{n}{2}) + n$, and according to master's theorem time complexity is $O(n\log n)$.

### Example 10. Reverse Nodes in k-Group
> [Leetcode: 25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

#### Solution
To solve this problem with $O(n)$ time complexity and $O(1)$ extra space (not accounting for the space for recursion call stack), solve this problem recursively like [Example 1](#example1-reverse-linked-list).  
