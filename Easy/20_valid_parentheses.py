"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "[" }
        for c in s:
            if c in closeToOpen: # checks keys which are closing parentheses
                if stack and stack[-1] == closeToOpen[c]:  # stack[-1] checks top of stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False    
