
# Minesweeper Game

This is a graphical implementation of the classic **Minesweeper** game using Python and the **Pygame** library. The game features a grid of cells with mines hidden randomly, and the objective is to uncover all cells that do not contain mines without triggering any mines.

## Features

- **Game Grid**: The game is played on an 8x8 grid, customizable if needed.
- **Mines**: A total of 10 mines are randomly placed within the grid.
- **Adjacent Mines**: Each cell shows a number indicating how many mines are in adjacent cells.
- **Game Over**: If a mine is revealed, the game ends with a "GAME OVER" message.
- **Recursive Reveal**: Cells with zero adjacent mines reveal all adjacent cells recursively.
- **Winning Condition**: The game is won when all non-mined cells are revealed.

## Requirements

### Software
- Python 3.x
- Pygame library

### Installation

To run this game, you need to install Python 3.x and the **Pygame** library.

#### Step 1: Install Pygame
You can install the required dependencies by running the following command:

```bash
pip install pygame
```

#### Step 2: Clone the repository
Clone this repository to your local machine using:

```bash
git clone https://github.com/your-username/minesweeper-game.git
```

#### Step 3: Run the Game

After installing the dependencies, navigate to the directory containing the `main.py` file and run it:

```bash
python main.py
```

### Game Controls

- **Left-click**: Reveals a cell. If you reveal a mine, the game ends.
- **Right-click (optional)**: You can implement a flagging feature where you mark suspected mines. However, this is not implemented in the current version.

### How to Play

1. **Starting the Game**: When you start the game, you will see a grid of cells. Each cell is initially hidden.
2. **Revealing Cells**: Click on any cell to reveal it. If the cell is safe, it will display a number showing how many mines are in adjacent cells.
3. **Uncovering Mines**: If you click on a cell that contains a mine, the game ends, and you will see a "GAME OVER" message.
4. **Safe Cells**: If the cell you click on has no adjacent mines, all connected safe cells will be revealed automatically.
5. **Winning the Game**: The game is won when all non-mined cells have been revealed. 

### Customization

- **Grid Size**: The default grid size is set to **8x8**, but you can change the `GRID_SIZE` variable to increase or decrease the size.
- **Mines**: The number of mines is set to **10** by default. You can adjust this in the `num_mines` variable in the `place_mines()` function.

## Game Design

### Grid Initialization

The grid is a 2D list where each element represents a cell. A value of `-1` represents a mine, and a positive integer represents the number of adjacent mines. The grid is initialized as follows:

```python
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
```

### Revealing Cells

The `reveal_cell()` function is responsible for revealing a cell when it is clicked. If the cell is empty (no adjacent mines), it recursively reveals neighboring cells:

```python
def reveal_cell(row, col):
    if grid[row][col] == 0:
        for dr, dc in DIRECTIONS:
            reveal_cell(row + dr, col + dc)
```
### Game Over Logic

If a mine is revealed, the game is set to **game_over = True**, and the "GAME OVER" message is displayed:

```python
def reveal_cell(row, col):
    if grid[row][col] == -1:
        global game_over
        game_over = True
```

### Drawing the Game

The `draw_grid()` function handles the rendering of the grid on the screen, and `draw_game_over()` displays the game over message:

```python
def draw_grid(screen):
    # Drawing logic for cells
    # Fill cells with appropriate colors based on the state (revealed or hidden)
```

## Project Structure

```
.
├── main.py               # Main game file containing the game logic
└── README.md             # This readme file
```

### File Breakdown

- **`main.py`**: The main script of the game. It handles:
  - Pygame setup and window initialization.
  - Logic for placing mines and calculating adjacent mines.
  - Event handling for mouse clicks and game over logic.
  - Rendering the grid and the game over message.

### Libraries Used

- **Pygame**: This game is built using the Pygame library, which is a set of Python modules designed for writing video games. It provides functionality for graphics, event handling, and user input.

## License

This project is open source and available under the [MIT License](LICENSE).

Feel free to modify or redistribute this project, but please include credit to the original authors.

## Contributions

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your improvements or fixes. Make sure to follow the contribution guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md).

---

### Credits

- **Author**: Your Name or Nickname
- **Contributors**: List of people who have contributed to the project.
