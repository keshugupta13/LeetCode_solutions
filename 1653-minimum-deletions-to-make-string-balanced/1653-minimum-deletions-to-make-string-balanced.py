class Solution(object):
    def minimumDeletions(self, s):
        stack = []
        count = 0
        for char in s:
            if char == 'a' and stack and stack[-1] == 'b':
                stack.pop()
                count += 1
            else:
                stack.append(char)
        return count

        """
        :type s: str
        :rtype: int
        """
        