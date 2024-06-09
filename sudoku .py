import random
import math

class Sudoku:
    def __init__(self, order):
        self.order = order
        self.size = order * order
        self.board = [[0] * self.size for _ in range(self.size)]

    def is_valid(self, row, col, num):
        for x in range(self.size):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False

        start_row, start_col = row - row % self.order, col - col % self.order
        for i in range(self.order):
            for j in range(self.order):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True

        row, col = empty
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0

        return False

    def find_empty_location(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def fill_diagonal_boxes(self):
        for i in range(0, self.size, self.order):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        nums = list(range(1, self.size + 1))
        random.shuffle(nums)
        for i in range(self.order):
            for j in range(self.order):
                self.board[row + i][col + j] = nums.pop()

    def remove_numbers(self, difficulty):
        attempts = difficulty * self.size * self.size // 10
        while attempts > 0:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            while self.board[row][col] == 0:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
            backup = self.board[row][col]
            self.board[row][col] = 0
            copy_board = [row[:] for row in self.board]
            if not self.solve():
                self.board[row][col] = backup
                attempts -= 1
            self.board = copy_board
            attempts -= 1

    def generate_puzzle(self, difficulty=5):
        self.board = [[0] * self.size for _ in range(self.size)]
        self.fill_diagonal_boxes()
        self.solve()
        self.remove_numbers(difficulty)
        return self.board

# Usage Example
order = 3
sudoku = Sudoku(order)
sudoku.generate_puzzle(difficulty=5)
sudoku.print_board()
print("\nSolving Sudoku...\n")
sudoku.solve()
sudoku.print_board()
