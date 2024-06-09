# Sudoku
This project involves creating an application to solve and generate N-order Sudoku puzzles.


# N-Order Sudoku Solver and Generator

## Overview

The N-Order Sudoku Solver and Generator project is a Python application that can solve and generate Sudoku puzzles of any order (e.g., 4x4, 9x9, 16x16). The application uses backtracking algorithms to solve puzzles and generate valid Sudoku boards.

## Features

- Solve Sudoku puzzles of various sizes.
- Generate Sudoku puzzles with adjustable difficulty.
- Validate Sudoku board configurations.
- Intuitive console-based interface for interaction.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/n-order-sudoku.git
    cd n-order-sudoku
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Create an instance of the `Sudoku` class with the desired order:
    ```python
    from sudoku import Sudoku
    order = 3  # For a standard 9x9 Sudoku
    sudoku = Sudoku(order)
    ```

2. Generate a new puzzle with a specified difficulty:
    ```python
    sudoku.generate_puzzle(difficulty=5)
    sudoku.print_board()
    ```

3. Solve the generated puzzle:
    ```python
    print("\nSolving Sudoku...\n")
    sudoku.solve()
    sudoku.print_board()
    ```

### Example

```python
from sudoku import Sudoku

order = 3  # For a standard 9x9 Sudoku
sudoku = Sudoku(order)

# Generate a puzzle
sudoku.generate_puzzle(difficulty=5)
sudoku.print_board()

# Solve the puzzle
print("\nSolving Sudoku...\n")
sudoku.solve()
sudoku.print_board()

