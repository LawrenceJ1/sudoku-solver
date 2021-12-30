class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #declaring variables
        empty_spaces = deque()
        possible_nums = {}
        self.nums = set(str(i) for i in range(1, 10))
        
        #getting all empty spaces
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_spaces.append((i, j))
        
        def get_possible_nums(i, j):
            """Gets all possible nums for an empty space."""
            possible_nums[(i, j)] = []
            square_row = i-i%3
            square_col = j-j%3
            for k in range(3):
                for l in range(3):
                    if board[square_row+k][square_col+l] != "." and board[square_row+k][square_col+l] in self.nums:
                        self.nums.remove(board[square_row+k][square_col+l])
            for k in range(9):
                if board[i][k] != "." and board[i][k] in self.nums:
                    self.nums.remove(board[i][k])
                if board[k][j] != "." and board[k][j] in self.nums:
                    self.nums.remove(board[k][j])
            possible_nums[(i, j)] += self.nums
            self.nums = set(str(i) for i in range(1, 10))
        
        def backtrack(index=0):
            if index == len(empty_spaces):
                return True
            r, c = empty_spaces[index][0], empty_spaces[index][1]
            get_possible_nums(r, c)
            if possible_nums[(r, c)]:
                for i in possible_nums[(r, c)]:
                    board[r][c] = str(i)
                    flag = backtrack(index+1)
                    if flag:
                        return True
                    else:
                        board[r][c] = "."
            return False
    
        backtrack()