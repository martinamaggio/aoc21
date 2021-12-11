# https://adventofcode.com/2021/
# day 11, puzzle 2

import numpy as np


def get_neighbors(position, board_size):
  rr, cc = position
  n = [(rr+1, cc), (rr-1, cc), (rr, cc+1), (rr, cc-1), (rr+1, cc+1), (rr+1, cc-1), (rr-1, cc+1), (rr-1, cc-1)]
  return list(filter(lambda pp: 0 <= pp[0] < board_size and 0 <= pp[1] < board_size, n))


with open('input.txt') as f:
  energy_levels = [line.rstrip() for line in f]

size = 10
answer = 0
step = 0

# parsing input
grid = np.zeros((size, size), dtype=int)
for r in range(size):
  for c in range(size):
    grid[r, c] = int(energy_levels[r][c])

while True:
  step += 1
  grid = grid + 1

  fired = set()
  to_fire = set([tuple(x) for x in np.argwhere(grid > 9).tolist()])

  while to_fire:
    current_position = to_fire.pop()
    if current_position not in fired:
      answer += 1
      for p in get_neighbors(current_position, size):
        grid[p] += 1
        if grid[p] > 9:
          to_fire.add(p)
      fired.add(current_position)

  for p in fired:
    grid[p] = 0

  if np.all(grid == 0):
     answer = step
     break

print("Answer: %d" % answer)
