class Solution(object):
    def longestValidParentheses(self, s):
        stack=[]
        length=0
        stack.append(-1)
        n=len(s)
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = max(length,i-stack[-1])
        return length

        