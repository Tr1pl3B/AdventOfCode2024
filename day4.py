import re

def find_xmas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Define all 8 possible directions
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1), # down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (-1, 1)  # up-right
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_word(grid, r, c, dr, dc):
                    count += 1

    return count

def check_word(grid, r, c, dr, dc):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    for i in range(len(word)):
        nr = r + dr * i
        nc = c + dc * i
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
            return False
    return True

# Read the input grid from the file
with open("day4input.txt", "r") as file:
    grid = [line.strip() for line in file]

# Find and count all occurrences of "XMAS"
count = find_xmas(grid)
print(count)