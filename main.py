from itertools import permutations, product
import time
from def_tiles import tiles  # Import tile definitions from external file


def rotate_tile(tile):
    """Generate all four possible rotations of a tile."""
    return [tile, tile[1:] + tile[:1], tile[2:] + tile[:2], tile[3:] + tile[:3]]


def is_valid_partial(grid, row, col):
    """Check if the current tile placement is valid so far, ensuring small parts match large parts."""
    if row > 0:
        if (grid[row - 1][col][2][0] != grid[row][col][0][0]) or (grid[row - 1][col][2][1] == grid[row][col][0][1]):
            return False
    if col > 0:
        if (grid[row][col - 1][1][0] != grid[row][col][3][0]) or (grid[row][col - 1][1][1] == grid[row][col][3][1]):
            return False
    return True


def rotate_grid(grid):
    """Generate all four 90-degree rotations of a 3x3 grid, rotating tiles as well."""
    return [
        grid,
        [[grid[2][0][3:] + grid[2][0][:3], grid[1][0][3:] + grid[1][0][:3], grid[0][0][3:] + grid[0][0][:3]],
         [grid[2][1][3:] + grid[2][1][:3], grid[1][1][3:] + grid[1][1][:3], grid[0][1][3:] + grid[0][1][:3]],
         [grid[2][2][3:] + grid[2][2][:3], grid[1][2][3:] + grid[1][2][:3], grid[0][2][3:] + grid[0][2][:3]]],
        [[grid[2][2][2:] + grid[2][2][:2], grid[2][1][2:] + grid[2][1][:2], grid[2][0][2:] + grid[2][0][:2]],
         [grid[1][2][2:] + grid[1][2][:2], grid[1][1][2:] + grid[1][1][:2], grid[1][0][2:] + grid[1][0][:2]],
         [grid[0][2][2:] + grid[0][2][:2], grid[0][1][2:] + grid[0][1][:2], grid[0][0][2:] + grid[0][0][:2]]],
        [[grid[0][2][1:] + grid[0][2][:1], grid[1][2][1:] + grid[1][2][:1], grid[2][2][1:] + grid[2][2][:1]],
         [grid[0][1][1:] + grid[0][1][:1], grid[1][1][1:] + grid[1][1][:1], grid[2][1][1:] + grid[2][1][:1]],
         [grid[0][0][1:] + grid[0][0][:1], grid[1][0][1:] + grid[1][0][:1], grid[2][0][1:] + grid[2][0][:1]]]
    ]


def remove_rotational_duplicates(solutions):
    """Remove solutions that are rotationally symmetrical."""
    unique_solutions = []
    seen = set()

    for solution in solutions:
        rotations = [tuple(map(tuple, rotate)) for rotate in rotate_grid(solution)]
        if not any(rot in seen for rot in rotations):
            unique_solutions.append(solution)
            seen.add(rotations[0])

    return unique_solutions


def backtrack(grid, tiles, used, solutions, row=0, col=0):
    """Backtracking solver with early validation, ensuring only available tiles are used."""
    if row == 3:
        solutions.append([row[:] for row in grid])  # Store a copy of the solution
        return

    next_row, next_col = (row, col + 1) if col < 2 else (row + 1, 0)

    for i, tile_variants in enumerate(tiles):
        if not used[i]:
            used[i] = True
            for tile in tile_variants:
                grid[row][col] = tile
                if is_valid_partial(grid, row, col):
                    backtrack(grid, tiles, used, solutions, next_row, next_col)
            used[i] = False


def solve_puzzle():
    """Find all possible valid configurations and remove rotationally symmetrical ones."""
    all_rotations = [rotate_tile(t) for t in tiles]
    grid = [[None] * 3 for _ in range(3)]
    used = [False] * 9
    solutions = []

    start_time = time.time()
    backtrack(grid, all_rotations, used, solutions)
    solutions = remove_rotational_duplicates(solutions)
    end_time = time.time()

    print(f"Found {len(solutions)} unique solutions in {end_time - start_time:.2f} seconds.")
    return solutions


solutions = solve_puzzle()
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
