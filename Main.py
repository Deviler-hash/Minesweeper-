import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the game window
GRID_SIZE = 8
CELL_SIZE = 40
MARGIN = 5
WIDTH = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN
HEIGHT = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Define colors
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Game variables
grid = []
revealed = []
game_over = False

# Directions for checking adjacent cells
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# --- Helper Function ---
def get_cell_coords(row, col):
    x = col * (CELL_SIZE + MARGIN) + MARGIN
    y = row * (CELL_SIZE + MARGIN) + MARGIN
    return x, y

# --- Initialize Game ---
def init_game():
    global grid, revealed, game_over
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    game_over = False
    place_mines()
    calculate_adjacent_mines()

def place_mines():
    mines_placed = 0
    num_mines = 10
    while mines_placed < num_mines:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if grid[row][col] != -1:
            grid[row][col] = -1  # -1 represents a mine
            mines_placed += 1

def calculate_adjacent_mines():
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] != -1:
                mine_count = 0
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and grid[nr][nc] == -1:
                        mine_count += 1
                grid[row][col] = mine_count

# --- Handle Cell Actions ---
def reveal_cell(row, col):
    if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE) or revealed[row][col]:
        return
    revealed[row][col] = True
    if grid[row][col] == 0:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            reveal_cell(row + dr, col + dc)
    elif grid[row][col] == -1:
        global game_over
        game_over = True

def handle_click(pos):
    if game_over:
        return
    mouse_x, mouse_y = pos
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            cell_x, cell_y = get_cell_coords(row, col)
            cell_rect = pygame.Rect(cell_x, cell_y, CELL_SIZE, CELL_SIZE)
            if cell_rect.collidepoint(mouse_x, mouse_y):
                print(f"Clicked on cell: (row={row}, col={col})")
                reveal_cell(row, col)
                return

# --- Drawing ---
def draw_grid(screen):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x, y = get_cell_coords(row, col)
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 2) # Cell border

            if revealed[row][col]:
                if grid[row][col] == -1:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, GRAY, rect)
                    if grid[row][col] > 0:
                        font = pygame.font.SysFont(None, 30)
                        text = font.render(str(grid[row][col]), True, BLUE)
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, BLUE, rect)

def draw_game_over(screen):
    font = pygame.font.SysFont(None, 70)
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# --- Main Game Loop ---
def main():
    global game_over
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Deviler")
    clock = pygame.time.Clock()
    init_game()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    handle_click(event.pos)

        draw_grid(screen)

        if game_over:
            draw_game_over(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()