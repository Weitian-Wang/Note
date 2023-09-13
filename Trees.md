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


#### Solution
#### Complexity

### Example.12 Kth Smallest Element in a BST
> [Leetcode 230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)  


#### Solution
#### Complexity

### Example.13 Construct Binary Tree from Preorder and Inorder Traversal
> [Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

#### Solution

#### Complexity