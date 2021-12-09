# https://adventofcode.com/2021/
# day 9, puzzle 1

import numpy as np


def get_neighbouring_locations(r, c, height, width):
  locations = set()
  if r > 0:          locations.add((r - 1, c))
  if r < height - 1: locations.add((r + 1, c))
  if c > 0:          locations.add((r, c - 1))
  if c < width - 1:  locations.add((r, c + 1))
  return locations


with open('input.txt') as f:
  heightmap = [line.rstrip() for line in f]

grid_height = len(heightmap)
grid_width = len(heightmap[0])
grid = np.zeros((grid_height, grid_width), dtype=int)

for r in range(grid_height):
  for c in range(grid_width):
    grid[r, c] = int(heightmap[r][c])

answer = 0

for r in range(grid_height):
  for c in range(grid_width):
    neighbors_locations = get_neighbouring_locations(r, c, grid_height, grid_width)
    neighbors = list(map(lambda x: grid[x[0]][x[1]], neighbors_locations))

    if all(grid[r][c] < neighbors):
      answer += grid[r][c] + 1

print("Answer: %d" % answer)
