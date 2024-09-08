def sudoku(puzzle):
    def is_valid(num, row, col):
        # Check if num is not in the current row, column, and 3x3 box
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if puzzle[i][j] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            puzzle[row][col] = num
                            if solve():
                                return True
                            puzzle[row][col] = 0
                    return False
        return True

    solve()
    return puzzle
