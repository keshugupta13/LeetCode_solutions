class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0:
            return 0
            
        if s[0]=="}" or s[0]== ")" or s[0]=="]":
            return 0
        
        if s[len(s)-1] == "{" or s[len(s)-1] == "[" or s[len(s)-1] == "(":
            return 0
            
        stack = []
        for i in s:
            if i=="{" or i=="(" or i=="[":
                stack.append(i)
                
            else:
                if len(stack) == 0:
                    return 0
                
                if i=="]":
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        return 0
                        
                elif i=="}":
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        return 0
                else:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        return 0
        if len(stack)==0:
            return 1
        else:
            return 0