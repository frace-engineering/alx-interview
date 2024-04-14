#!/usr/bin/python3
"""The queen game"""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    """Check upper left diagonal"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    """Check upper right diagonal"""
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(N):
    """Setting the board if N is integer"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)

    for sol in solutions:
        print_solution(sol)


def solve_util(board, row, N, solutions):
    """Solve util function"""
    if row == N:
        solutions.append([''.join(row) for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_util(board, row + 1, N, solutions)
            board[row][col] = '.'


def print_solution(solution):
    """Print the row"""
    for row in solution:
        print(row)
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_n_queens(sys.argv[1])
