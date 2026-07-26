from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracketMapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = deque() # stack object
        
        for char in s: 
            if char in bracketMapping:
                if stack and stack[-1] == bracketMapping[char]:
                    stack.pop() # removes open bracket if closing bracket is found
                else:
                    return False
            else:
                stack.append(char) # adds opening bracket to stack

        return True if not stack else False