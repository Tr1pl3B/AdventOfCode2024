def find_xmas_pattern(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Define all 8 possible orientations for the X-MAS pattern
    patterns = [
        [(0, 0), (1, -1), (2, -2), (1, 1), (2, 2)],  # MAS down-left, MAS down-right
        [(0, 0), (1, 1), (2, 2), (1, -1), (2, -2)],  # MAS down-right, MAS down-left
        [(0, 0), (-1, -1), (-2, -2), (-1, 1), (-2, 2)],  # MAS up-left, MAS up-right
        [(0, 0), (-1, 1), (-2, 2), (-1, -1), (-2, -2)],  # MAS up-right, MAS up-left
        [(0, 0), (1, -1), (2, -2), (-1, 1), (-2, 2)],  # MAS down-left, MAS up-right
        [(0, 0), (1, 1), (2, 2), (-1, -1), (-2, -2)],  # MAS down-right, MAS up-left
        [(0, 0), (-1, -1), (-2, -2), (1, 1), (2, 2)],  # MAS up-left, MAS down-right
        [(0, 0), (-1, 1), (-2, 2), (1, -1), (2, -2)]  # MAS up-right, MAS down-left
    ]

    for r in range(rows):
        for c in range(cols):
            for pattern in patterns:
                if check_xmas_pattern(grid, r, c, pattern):
                    count += 1

    return count

def check_xmas_pattern(grid, r, c, pattern):
    rows = len(grid)
    cols = len(grid[0])
    word = "MAS"
    for i, (dr, dc) in enumerate(pattern):
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i % 3]:
            return False
    return True

# Read the input grid from the file
with open("day4input.txt", "r") as file:
    grid = [line.strip() for line in file]

# Find and count all occurrences of the X-MAS pattern
count = find_xmas_pattern(grid)
print(count)