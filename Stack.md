## Stack
- [Stack](#stack)
  - [Introduction](#introduction)
    - [Characteristics of Stack](#characteristics-of-stack)
    - [Applications of Stack](#applications-of-stack)
  - [Example.1 Parenthesis Matching](#example1-parenthesis-matching)
    - [Solution](#solution)
  - [Example.2 Min Stack](#example2-min-stack)
  - [Example.3 Reverse Polish](#example3-reverse-polish)
  - [Example.4 Generate Parentheses](#example4-generate-parentheses)
  - [Example.5 Daily Temperature](#example5-daily-temperature)
  - [Example.6 Largest Rectangle In Histogram](#example6-largest-rectangle-in-histogram)

### Introduction
#### Characteristics of Stack
The addition and removal of elements take place at stack top. The priciple by which the stack is ordered is called last-in-first-out (LIFO).  
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
### Example.1 Parenthesis Matching
> [Leetcode: 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)  
 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#### Solution
Use the FILO/LIFO property of stack to solve this problem.  
```
Iterate throught the input string.  
- If input character is opening bracket, push to stack.  
- Else if input characeter is closing bracket, check if matching opening bracket in stack top, if so pop element.  
- Finally, check if the stack is empty, which means no opening brackets are left unmatched.  
```

### Example.2 Min Stack
> [Leetcode: 155. Min Stack](https://leetcode.com/problems/min-stack/)  

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

### Example.3 Reverse Polish
### Example.4 Generate Parentheses
### Example.5 Daily Temperature
### Example.6 Largest Rectangle In Histogram

