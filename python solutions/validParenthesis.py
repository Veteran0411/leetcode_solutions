# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

def isValid(s):
    close=[")","}","]"]
    open=["(","{","["]
    dic={
        "(":")","{":"}","[":"]",
    }
    stack=[]
    if s and s[0] in close:
        return False
    for i in s:
        if i in open:
            stack.append(i)
        else:
            if not stack or dic.get(stack[-1])!=i:
                return False
            stack.pop()
            
    return len(stack)==0

if __name__=="__main__":
    s=input("enter the string to check the validity: ")
    print(isValid(s))