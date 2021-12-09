# https://adventofcode.com/2021/
# day 9, puzzle 2

import numpy as np
import functools


def get_neighbouring_locations(r, c, height, width):
  locations = set()
  if r > 0:          locations.add((r - 1, c))
  if r < height - 1: locations.add((r + 1, c))
  if c > 0:          locations.add((r, c - 1))
  if c < width - 1:  locations.add((r, c + 1))
  return locations


def get_basin(r, c, height, width, grid):

  start_location = (r, c)

  def get_added_locations(loc):
    added_locations = set()
    for p in get_neighbouring_locations(loc[0], loc[1], height, width):
      if grid[p] != 9:
        added_locations.add(p)
    return added_locations

  locations, locations_new = set(), set()
  locations_new.add(start_location)
  while locations != locations_new:
    locations = locations_new
    for p in locations_new:
      locations_new = locations_new.union(get_added_locations(p))
  return locations_new


with open('input.txt') as f:
  heightmap = [line.rstrip() for line in f]

grid_height = len(heightmap)
grid_width = len(heightmap[0])
grid = np.zeros((grid_height, grid_width), dtype=int)

for r in range(grid_height):
  for c in range(grid_width):
    grid[r, c] = int(heightmap[r][c])

basin_sizes = list()

for r in range(grid_height):
  for c in range(grid_width):

    # first find the minimum points
    neighbors_locations = get_neighbouring_locations(r, c, grid_height, grid_width)
    neighbors = list(map(lambda x: grid[x[0]][x[1]], neighbors_locations))

    if all(grid[r][c] < neighbors):
      basin = get_basin(r, c, grid_height, grid_width, grid)
      basin_sizes.append(len(basin))

relevant_sizes = sorted(basin_sizes, reverse=True)[:3]
answer = functools.reduce(lambda x, y: x*y, relevant_sizes)
print("Answer: %d" % answer)
