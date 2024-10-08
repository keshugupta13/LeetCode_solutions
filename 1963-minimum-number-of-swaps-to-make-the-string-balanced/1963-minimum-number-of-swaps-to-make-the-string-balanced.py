class Solution(object):
    def minSwaps(self, s):
        stack = []
        unmatched = 0
        
        for bracket in s:
            if bracket == '[':
                stack.append(bracket)
            elif bracket == ']':
                if stack:
                    stack.pop()
                else:
                    unmatched += 1
        
        return (unmatched + 1) // 2