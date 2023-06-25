#!/usr/bin/python3
"""Task 101"""
import sys
import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the top left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check if there is a queen in the top right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens(board, row+1, n, solutions)
            board[row][col] = '.'

            
def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join(row))
        print()
        

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == '__main__':
    main() 
"""End Task"""
