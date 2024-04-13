#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(board)])
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0 # Backtrack

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
 
   
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    
    for sol in solutions:
        print(sol)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
