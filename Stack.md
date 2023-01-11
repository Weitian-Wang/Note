## Stack
- [Stack](#stack)
  - [Introduction](#introduction)
    - [Characteristics of Stack](#characteristics-of-stack)
    - [Applications of Stack](#applications-of-stack)
  - [Example.1 Parenthesis Matching](#example1-parenthesis-matching)
    - [Solution](#solution)
  - [Example.2 Min Stack](#example2-min-stack)
    - [Solution](#solution-1)
  - [Example.3 Reverse Polish](#example3-reverse-polish)
    - [Solution](#solution-2)
  - [Example.4 Generate Parentheses](#example4-generate-parentheses)
    - [Solution](#solution-3)
  - [Example.5 Daily Temperature](#example5-daily-temperature)
    - [Solution](#solution-4)
  - [Example.6 Car Fleet](#example6-car-fleet)
    - [Solution](#solution-5)
  - [Example.7 Largest Rectangle In Histogram](#example7-largest-rectangle-in-histogram)
    - [Solution](#solution-6)

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
Iterate throught the input string.  
- If input character is opening bracket, push to stack.  
- Else if input characeter is closing bracket, check if matching opening bracket in stack top, if so pop element.  
- Finally, check if the stack is empty, which means no opening brackets are left unmatched.  

### Example.2 Min Stack
> [Leetcode: 155. Min Stack](https://leetcode.com/problems/min-stack/)  

Design a stack that supports push, pop, top, and retrieving the minimum element in **constant time**.
#### Solution
Use one **data stac**k to store the value and another **auxiliary stack** to store the minimum value at current state.  
- Top: return stack value located at data stack top
- Pop: pop from both stack
- Min: value stored at auxiliary stack top
- Push: push value to data stack, push the minimum of new value & mini value to auxiliary stack
### Example.3 Reverse Polish
> [Leetcode 150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)  

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.  
Evaluate the expression. Return an integer that represents the value of the expression.  
#### Solution
Use one stack to store operant. Iterate through the tokens.  
- If token is operand, push to stack.
- Else if token is operator, pop two operands from stack and calculate, push result to operand stack.  
> Division truncates toward zero: math.floor truncates results towards zero for positive number division, but truncates away from zero for negative number division. User int() conversion for this problem.  
> However Python int() conversion behavior is unpredicable, avoid in production codes.   
> - int(5.9) = 5
> - int(5.9999999999999999999) = 6  

### Example.4 Generate Parentheses
> [Leetcode 22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)  

Given n pairs of parentheses, write a function to generate all combinations of **well-formed** parentheses.
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```
#### Solution
Depth first search & the LIFO push/pop operation of stack.  
Count number of opening brackets and closing bracks with two seperate variables.  
For each DFS recursion:  
- If open + close == n * 2, add combination to result list & return
- If open < n, push a opening bracket to stack, DFS then pop from stack
- If close < open, push a closing bracket to stack, DFS then pop from stack

### Example.5 Daily Temperature
> [Leetcode 739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the **number of days** you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.  

#### Solution
Monotonically decreasing stack & store extra information in stack.  
1. Initiate an array of the same size with 0s, and an empty stack
2. Iterater through array of temperatures:  
- If temperature lower than stack top, push temperature and index to stack
- If and while temperature, pop top and calculate the number of days = current idx - poped idx, write result to result array 
 
### Example.6 Car Fleet
> [Leetcode 853. Car Fleet](https://leetcode.com/problems/car-fleet/)  

There are ``n`` cars going to the same destination along a one-lane road. The destination is ``target`` miles away.

You are given two integer array ``position`` and ``speed``, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

See full problem description via the link.

Return the **number of car fleets** that will arrive at the destination.
#### Solution
Monotonic stack.  
1. Sort the car position and speed according to position.
> Use zip() function to create truple of iterables:  
> zip(position, speed) -> [(p0, s0), (p1, s1), ..., (pn-1, sn-1)]  

2. Calculate the time needed for each car to reach destination, put in a ``time`` array
> Cars that reach destination in shorter time will catch up and form fleet with slower cars ahead of them.  

3. Initiate a monotonically decreasing stack
4. Iterate through ``time`` array, pop until stack top larger than element, then push element to stack
5. Return the number of element in the stack, which equals to the number of car fleets

### Example.7 Largest Rectangle In Histogram
> [Leetcode 84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)  

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#### Solution
Monotonically increasing stack + extra information to store the width of current height.  
The rectangle of given height can extend to the right, only when right elements are higher.  
Initialize a monotonically increasing stack with width as extra data field.  
Iterate through the array of heights  
- Push to stack when stack empty or height greater equal to stack top
- Pop from stack when height lower than stack top, keep track of cumulative width, calculate area
