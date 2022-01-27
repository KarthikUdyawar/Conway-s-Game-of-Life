from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from itertools import product
import random
import sys
import time
import csv

import pygame

# * Constents
FPS = 60
CELL_SIZE = 10
GRID_SIZE = width, height = (100, 50)
SCREEN_SIZE = GRID_SIZE[0] * CELL_SIZE, GRID_SIZE[1] * CELL_SIZE

# * Colour sets
GREEN = (50, 200, 50)
BLACK = (0, 0, 0)

# * Pygame init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Conway's Game of Life")
Icon = pygame.image.load("./images/icon.png")
pygame.display.set_icon(Icon)


def create_grid(width: int, height: int, randomize: bool = False) -> "list[list[int]]":
    """Generates grid with required width and height

    Args:
        width (int): Width of the grid
        height (int): height of the grid
        randomize (bool, optional): If it is set True then it will generate random cluster
                                    else blank grid. Defaults to False.

    Returns:
        list[list[int]]: 2D list repression of a grid containing 0 and 1
    """
    return (
        [[random.choice([0, 1]) for _ in range(height)] for _ in range(width)]
        if randomize
        else [[0 for _ in range(height)] for _ in range(width)]
    )


def get_neighbours(x: int, y: int, grid: "list[list[int]]") -> list:
    """Gets the list of live neighbors in the particular cell

    Args:
        x (int): X postion of the cell
        y (int): Y postion of the cell
        grid ([type]): 2D list repression of grid

    Returns:
        list: Live neighbours in the particular cell
    """
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:  # ? Not including itself
                nx = (x + dx) % width
                ny = (y + dy) % height
                neighbour = grid[nx][ny]
                neighbours.append(neighbour)

    return neighbours


def generator(grid) -> "list[list[int]]":
    """Main function for Conway's Game of Life

    Args:
        grid ([type]): 2D list repression of grid

    Returns:
        list[list[int]]: 2D list of new generated grid
    """
    new_grid = create_grid(width, height)
    coords = product(range(width), range(height))
    for x, y in coords:
        neighbors = get_neighbours(x, y, grid)
        alive_num = sum(neighbors)
        state = grid[x][y]

        # ? Any live cell with two or three live neighbours survives.
        if state == 1 and alive_num in [2, 3]:
            new_grid[x][y] = 1
        # ? Any dead cell with three live neighbours becomes a live cell.
        elif state == 0 and alive_num in [3]:
            new_grid[x][y] = 1
        # ? All other live cells die in the next generation.
        # ? Similarly, all other dead cells stay dead.
        else:
            new_grid[x][y] = 0

    return new_grid


def draw_cell() -> None:
    """Draw a cell on the grid"""
    for x, y in product(range(width), range(height)):
        coords = ((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE)
        if grid[x][y]:
            pygame.draw.circle(screen, GREEN, coords, CELL_SIZE / 2)


def drag_mouse(mouse_dragging: bool) -> None:
    """Edit the cells states in a grid

    Args:
        mouse_dragging (bool): Action of mouse
    """
    if mouse_dragging:
        x, y = pygame.mouse.get_pos()
        col, row = x // CELL_SIZE, y // CELL_SIZE
        grid[col][row] = 1 if grid[col][row] == 0 else 0


# * Game initiation
previous_state = time.time()
grid = create_grid(width, height, randomize=True)
pause = True
mouse_dragging = False
running = True

# * Main loop
if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ? Press Enter to toggle pause
                if event.key == pygame.K_RETURN:
                    pause = not pause

                # ? Press R key to reset the randome grid
                if event.key == pygame.K_r:
                    grid = create_grid(width, height, randomize=True)

                # ? Press C key to clear the grid
                if event.key == pygame.K_c:
                    grid = create_grid(width, height, randomize=False)
                    
                # ? Press S key to save the grid
                if event.key == pygame.K_s:
                    with open('grid_map.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows([list(x) for x in zip(*grid)])
                        print("Save")

            # ? Press or hold left mouse button to toggle the state of cell
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_dragging = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_dragging = True

            # ? Quit system
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        drag_mouse(mouse_dragging)

        # ? Refresh
        if time.time() - previous_state < 1 / FPS:
            continue

        previous_state = time.time()
        screen.fill(BLACK)

        if not pause:
            grid = generator(grid)

        draw_cell()

        pygame.display.flip()
