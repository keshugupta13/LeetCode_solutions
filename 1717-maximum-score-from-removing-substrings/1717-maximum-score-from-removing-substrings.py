class Solution(object):
    def maximumGain(self, s, x, y):
        res = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        stack = []
        for char in s:
            if char == top[1] and stack and  stack[-1] == top[0]:
                res += top_score
                stack.pop()
            else:
                stack.append(char)

        new_stack = []
        for char in stack:
            if char == bot[1] and new_stack and new_stack[-1] == bot[0]:

                res += bot_score
                new_stack.pop()
            else:
                new_stack.append(char)
        return res


        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        