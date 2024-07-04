class Solution(object):
    def solveSudoku(self, board):
        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    # Check if the cell is empty
                    if board[i][j] == '.':
                        for c in '123456789':  # Try numbers from 1 to 9
                            if is_valid(i, j, c):
                                board[i][j] = c
                                
                                if solve():
                                    return True
                                else:
                                    # Backtracking
                                    board[i][j] = '.'
                        return False
            return True
            
        def is_valid(row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            return True
        
        return solve()
        
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        