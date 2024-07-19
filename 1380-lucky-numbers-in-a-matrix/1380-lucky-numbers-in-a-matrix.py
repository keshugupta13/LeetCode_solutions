class Solution(object):
    def luckyNumbers (self, matrix):
        row_mins = []
        for row in matrix:
            row_mins.append(min(row))

        rows = len(matrix)
        cols = len(matrix[0])
        luckies = []
        for j in range(0,cols):
            col = []
            for i in range(0,rows):
                col.append(matrix[i][j])
            if max(col) in row_mins:
                luckies.append(max(col))
        return luckies
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        