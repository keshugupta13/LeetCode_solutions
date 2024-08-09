class Solution(object):
    def valid(self,matrix):
        visited = {}
        expected_sum = 0

        for i in range(3):
            row_sum = 0
            for j in range(3):
                num =  matrix[i][j]
                if 1<=num<=9 and num not in visited:
                    visited[num] = True
                else:
                    return False
                
                row_sum += num

            if i == 0:
                expected_sum = row_sum
            else:
                if expected_sum != row_sum:
                    return False
                
            
 
        for  j in range(3):
            col_sum = 0
            for i in range(3):
                num =  matrix[i][j]
                col_sum += num

            if j == 0:
                expected_sum = col_sum
            else:
                if expected_sum != col_sum:
                    return False
            
        diag1_sum = 0
        diag2_sum = 0
        for i in range(3):
            diag1_sum += matrix[i][i]
            diag2_sum += matrix[i][2-i]
        
        if diag1_sum != expected_sum or diag2_sum != expected_sum:
            return False
        
        return True
                
    def numMagicSquaresInside(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        count = 0

        if row < 3 or col < 3:
            return 0

        for i in range(row-2):
            for j in range(col-2):
                for x in range(3):
                    submatrix = [matrix[i][j:j+3], matrix[i+1][j:j+3], matrix[i+2][j:j+3]]
                if self.valid(submatrix):
                    count += 1
        return count



        """
        :type grid: List[List[int]]
        :rtype: int
        """
        