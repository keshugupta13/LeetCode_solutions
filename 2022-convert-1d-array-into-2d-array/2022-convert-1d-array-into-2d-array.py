class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []
        
        res = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[index])
                index += 1
            res.append(row)
        return res
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        