class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [""] * numRows 
        index = 0
        step = 1

        for i  in s:
            L[index] += i

            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1

            index += step
        return "".join(L)

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        