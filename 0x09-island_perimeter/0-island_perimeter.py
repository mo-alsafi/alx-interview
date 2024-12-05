def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over every cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check all four directions (up, down, left, right)
                # Up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

