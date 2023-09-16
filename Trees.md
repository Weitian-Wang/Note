## Trees
- [Trees](#trees)
	- [Introduction](#introduction)
		- [DFS \& BFS](#dfs--bfs)
			- [DFS](#dfs)
			- [BFS](#bfs)
		- [Traversals](#traversals)
			- [Inorder](#inorder)
			- [Preorder](#preorder)
			- [Postorder](#postorder)
	- [Types of Tree Questions](#types-of-tree-questions)
	- [Example.1 Invert Binray Tree](#example1-invert-binray-tree)
		- [Solution](#solution)
		- [Complexity](#complexity)
	- [Example.2 Maximum Depth of Binary Tree](#example2-maximum-depth-of-binary-tree)
		- [Solution](#solution-1)
		- [Tricks to Talk it Through in Interview](#tricks-to-talk-it-through-in-interview)
		- [Complexity](#complexity-1)
	- [Example.3 Diameter of Binary Tree](#example3-diameter-of-binary-tree)
		- [Solution](#solution-2)
		- [Complexity](#complexity-2)
	- [Example.4 Balanced Binary Tree](#example4-balanced-binary-tree)
		- [Solution](#solution-3)
		- [Complexity](#complexity-3)
	- [Example.5 Same Tree](#example5-same-tree)
		- [Solution](#solution-4)
		- [Complexity](#complexity-4)
	- [Example.6 Subtree of Another Tree](#example6-subtree-of-another-tree)
		- [Solution](#solution-5)
		- [Complexity](#complexity-5)
	- [Example.7 Lowest Common Ancestor of a Binary Search Tree](#example7-lowest-common-ancestor-of-a-binary-search-tree)
		- [Solution](#solution-6)
		- [Complexity](#complexity-6)
	- [Example.8 Binary Tree Order Level Traversal](#example8-binary-tree-order-level-traversal)
		- [Solution](#solution-7)
		- [Complexity](#complexity-7)
	- [Example.9 Binary Tree Right Side View](#example9-binary-tree-right-side-view)
		- [Solution](#solution-8)
		- [Complexity](#complexity-8)
	- [Example.10 Count Good Nodes in Binary Tree](#example10-count-good-nodes-in-binary-tree)
		- [Solution](#solution-9)
		- [Complexity](#complexity-9)
	- [Example.11 Validate Binary Search Tree](#example11-validate-binary-search-tree)
		- [Solution](#solution-10)
		- [Complexity](#complexity-10)
	- [Example.12 Kth Smallest Element in a BST](#example12-kth-smallest-element-in-a-bst)
		- [Solution](#solution-11)
		- [Complexity](#complexity-11)
	- [Example.13 Construct Binary Tree from Preorder and Inorder Traversal](#example13-construct-binary-tree-from-preorder-and-inorder-traversal)
		- [Solution](#solution-12)
		- [Complexity](#complexity-12)
	- [Example.14 Binary Tree Maximum Path Sum](#example14-binary-tree-maximum-path-sum)
		- [Solution](#solution-13)
		- [Complexity](#complexity-13)
	- [Example.15 Serialize and Deserialize Binary Tree](#example15-serialize-and-deserialize-binary-tree)
		- [Solution](#solution-14)
		- [Complexity](#complexity-14)


### Introduction
#### DFS & BFS
##### DFS
Tree problems usually can be handled recursively. As the definition of trees is recursive - the child of a tree node can be viewed as the root of the subtree.
##### BFS
When travese the tree in level order. Use a queue to store nodes from current level, then visit all of their children. Repeat the enqueue dequeue process with the child nodes.  
#### Traversals
##### Inorder
Left(recursively) - Parent - Right(recursively)
##### Preorder
Parent - Left -  Right  
Preorder traversal can be use to create a copy of the tree.  
##### Postorder
Left - Right - Parent
### Types of Tree Questions
1. Basic Traversal
2. Binary Search Tree
3. Tree Validation
4. Path Problem

### Example.1 Invert Binray Tree
> [Leetcode: 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)  

Given the `root` of a binary tree, invert the tree and return its `root`.  

#### Solution
For each node we invert its left and right child, and repeat the same process for it children. The subproblems are the same as the orginal problem.

#### Complexity
Time complexity $O(n)$, recursion stack depth $O(m)$, where $n$ is number of nodes in the tree and m is the height/depth of the tree.  
> Height and depth of a tree are equal.  
> Height and depth of a tree node can be different.  

### Example.2 Maximum Depth of Binary Tree
> [Leetcode: 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the `root` of a binary tree, return its *maximum depth*, which is the number of nodes along the longest path from the root node down to the farthest leaf node.  

#### Solution
The max depth of a node is the maximum of the max depth of its left subtree and right subtree plus one. The definition of maximum depth is a recursive definition.
#### Tricks to Talk it Through in Interview
1. Base Cases: Trees with 0 node or 1 node
2. Come up with the recursive definition
3. Translate the recursive definition to code
4. On paper dry run with test cases
6. Complexity analysis
7. 
#### Complexity
Time complexity $O(n)$, recursion stack depth $O(m)$, where $n$ is number of nodes in the tree and m is the height/depth of the tree.  

### Example.3 Diameter of Binary Tree
> [Leetcode: 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Given a `root` of a binary tree, return the length of the *diameter* of the tree.  
The *diameter* of a tree is the **length** of the longest path between to nodes. This path may not pass through the `root`.   
The **length** of the path between two nodes is represented by the number of edges between them.  

#### Solution
The longest path that passes throught the root has the length of 
$$\text{height of left subtree} + \text{height of right subtree}$$  
Use a global variable to track longest pass whilst recursively calculating the depth.  

#### Complexity
Time complexity $O(n)$, recursion stack depth $O(m)$, where $n$ is number of nodes in the tree and m is the height/depth of the tree.  

### Example.4 Balanced Binary Tree
> [Leetcode: 110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)  

Given the binary tree, determin if it's height-balanced.
#### Solution
The definition of balanced binray tree: the depth of the two subtrees of **every** node never differs by more than one.  

Recursively calculating the depth of the subtree, comparing the depth of left and right tree in the process.
#### Complexity
Time complexity $O(n)$, recursion stack depth $O(m)$, where $n$ is number of nodes in the tree and m is the height/depth of the tree.  

### Example.5 Same Tree
> [Leetcode: 100. Same Tree](https://leetcode.com/problems/same-tree/)

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. 

#### Solution
Check all the nodes with any order iteration method. For each pair of nodes, check if they have the same value, then recursively check both left and right subtrees.  
Edge case: 
1. Both nodes are `None`, reached leaf nodes
2. One of the two nodes is `None`, different structure

#### Complexity
Time complexity $O(n)$, recursion stack depth $O(m)$, where $n$ is number of nodes in the tree and m is the height/depth of the tree. 

### Example.6 Subtree of Another Tree
> [Leetcode: 572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

Given the roots of two binary trees `root` and `subroot`, check if there is a subtree of `root` that has the same structure and value with `subroot`.  

#### Solution
Base on example 5 we know how to detect if two trees are the same. Iterate every node in `root` and check if the subtree with that node as root is the same as tree `subroot`.  
Either recursive or iterative traversal of all nodes works fine.  
#### Complexity
Worst case $O(m*n)$, where $m$ is the number of nodes in `root`, $n$ is the number of nodes in `subroot`.

### Example.7 Lowest Common Ancestor of a Binary Search Tree
> [Leetcode: 235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Lowest common ancestor of node `p` and `q` is the lowest node that has both of them as descendents. A node can be a descendent of itself.  
#### Solution
In a Binary Search Tree, the lowest common ancestor is the first nodes that split the two targets (inclusive).  

That is to say if `t` is the LCA of `p` and `q`, where `p` is a smaller node than `q`, `p` has to be on `t`'s left subtree and `q` has to be `t`'s right subtree. One exception is that `p` or `q` is own ancestor.  

1. Swap `p` and `q` if necessary to ensure `p.val` smaller than `q.val`.  
2. Start `node` from `root`
   - if `p.val` < `q.val` < `node.val`, which means both `p` and `q` are on the left subtree, recursively search `node.left`
   - if `node.val` < `p.val` < `q.val`,  which means both `p` and `q` are on the right subtree, recursively search `node.right`
   - else `node` is the lowest common ancestor as it splits `p` and `q`

#### Complexity
The solution works like searching in a BST, time complexity $O(\log n)$. Where n $n$ is the number of nodes in BST.

### Example.8 Binary Tree Order Level Traversal
> [Leetcode 102. Binary Tree Order Level Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#### Solution
Broadth first search with a queue. 

#### Complexity
As we go through each node once the time complexity is $O(n)$ where n is the total number of nodes in the tree.

### Example.9 Binary Tree Right Side View
> [Leetcode 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)  

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#### Solution
is problem is a variant of problem 8. Instead of all the nodes, store the value of the right most node at each level. 
#### Complexity
$O(n)$ as we visit each node exactly once.  

### Example.10 Count Good Nodes in Binary Tree
> [Leetcode 1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)  

Given the binary tree `root`, a node `X` in the tree is named **good** if in the path from `root` to `X` there are no nodes with a value greater than `X`.  
Return the number of **good** nodes in the binary tree.  

#### Solution
Use a global counter to keep track of the number of good nodes. Traverse the tree and use a variable to record the minimum value on the path.  

If value of current node is smaller than the minimum on path, its a good node. Increase the global counter and update the minimum value.  
#### Complexity
$O(n)$ where $n$ is the number of nodes in the binary tree.  

### Example.11 Validate Binary Search Tree
> [Leetcode 98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)  

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).  

Definition of **valid BST**: 
1. All nodes on the left subtree of a node have smaller keys than the node
2. All nodes on the right subtree of a node have larger keys than the node
3. Both left and right subtrees are valid binary search trees

#### Solution
As we can see the definition of BTS is recursive. Therefore the validity of a BST can be checked recursively.  
1. Start with `root` node, it can have any key between $-\infty$ and $+\infty$, set as its lower and upper bound
2. As we traverse the left subtree of a node, update the upper bound with the node's value
3. As we traverse the right subtree of a node, update the lower bound with the node's value
Repeat the process with preorder traversal until we checked every node.  

```python
def checkValid(node, lower, upper):
	# leaf node
	if not node:
		return True
	# current node valid 
	if lower < node.val < upper:
		return checkValid(node.left, lower, node.val) and checkValid(node.right, node.val, upper)
	# node invalid
	else:
		return False

# call checkValid(root, float('-inf'), float('inf'))
```
#### Complexity
$O(n)$ where $n$ is the number of nodes in the tree. 

### Example.12 Kth Smallest Element in a BST
> [Leetcode 230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)  

Given the `root` of a binary tree, and an integer $k$, return the $k^{th}$ smallest value (1-indexed) of all the values of the tree nodes. 

#### Solution
The inorder traversal of a binary search tree returns the values in a ascending oreder. 
Few methods to retrieve the $k^{th}$ smallest value:
- Put all values in a list and access $k^{th}$ with index
- Push value into a min heap of size k when traversing the tree
- Use a counter and global variable to record the $k^{th}$ smallest value

#### Complexity
Time complexity $O(n)$ where $n$ is the total number of nodes in the tree. Space complexity varies depending on the method.  

### Example.13 Construct Binary Tree from Preorder and Inorder Traversal
> [Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Given two integer arrays `preorder` and `inorder` where `preoreder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.  

#### Solution
1. Apparently the first node in the `preorder` corresponds to the value of the `root` node.  
2. The array `inorder` can be divided into two subarrays by `root`, where the left subarray contains all node values from `root`'s left subtree and the right subarray contains all node values from `root`'s right subtree. 
3. Edge case: if any subarray is empty the respective subtree is a `None` node
4. Recursively solve both left and right subtrees

#### Complexity
$O(n)$ where $n$ is the total number of nodes. Worst case recursion depth $O(n)$ for binary trees that are skewed to one side.


### Example.14 Binary Tree Maximum Path Sum
> [Leetcode 124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes has a edge connecting them. A node can only appear in the sequence **at most once**.  
The **path sum** of path is the sum of the node's values in the path.  
Given the `root` of a binary tree return the maximum **path sum** of any none empty path.  
#### Solution
For any given tree, the maximum path sum can be produced from:
1.  A path that includes `root`
2.  A path on its left subtree
3.  A path on its right subtree
This applies for all of its subtrees.  

We could use a global variable to track the overall maximum path sum.  
In each recursive step, we return the maximum of the following three values to the parent node:
1. A path sum containing current node and nodes from its left subtree
2. A path sum containing current node and nodes form its right subtree
3. 0, if all pathes containing current node have a negative sum, discard this path entirely
> The partial path with nodes from nodes from **either** left or right subtree, so that the subroot is not duplicated when the parent node incorporate it in its path.  

Solution code:  
```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
		# none empty path, include a path even the sum is negative
        rst = float('-inf')

        def recurSum(node):
            nonlocal rst
            if not node:
                return 0
            left = recurSum(node.left)
            right = recurSum(node.right)
            rst = max(rst, left+right+node.val)
			# the return value is nonnegative
            return max(max(left, right) + node.val, 0)
        
        recurSum(root)
        return rst
```

#### Complexity
Time complexity of the solution is $O(n)$ where $n$ is the total number of nodes in the tree.  

### Example.15 Serialize and Deserialize Binary Tree
> [Leetcode 297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

Design a algorithm to serialize and deserialize a binary tree. Ensure that a binary tree can be serialized in to string and this string can be deserialized to the original binary tree structure.  
#### Solution
Initial thought:  
Use the recursive construction method from [Example.13 Construct Binary Tree from Preorder and Inorder Traversal](#example13-construct-binary-tree-from-preorder-and-inorder-traversal). However as the nodes values are not unique in this problem, the forementioned solution can produce faulty results.

Any Recursive Order traversal:  
Keep record all nodes in the tree including all the `None` nodes when traversing the binary tree in which ever order. Reconstruct the binary tree in the same traverse order.  
> Why this method works but in Example.13 both `inorder` and `preorder` are required? The extra `None` nodes contains enough information for reconstructing the binary tree.  
> The utilization of `None` nodes is also the downside of this solution. As the tree gets larger, there is a large number of `None` nodes at the lowest level, slowing down the deserializing process.  

Level order traversal:  
Serialize all nodes in the binary tree including all the `None` nodes in the level order traversal order. Deserialize the tree from the string with level order traversal.  

#### Complexity
Time complexity of the all the solutions above is $O(n)$ where $n$ is the number of nodes on the binary tree including `None` nodes.  