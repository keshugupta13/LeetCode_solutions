class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                rev = []
                while stack and stack[-1] != '(':
                    rev.append(stack.pop())
                stack.pop()  # pop the '(' from the stack
                
                for char in rev:
                    stack.append(char)
        
        return "".join(stack)

        