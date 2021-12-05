# https://adventofcode.com/2021/
# day 5, puzzle 2
import numpy as np
import math

# define sign function
sign = lambda x: 0 if x == 0 else int(math.copysign(1, x))

with open('input.txt') as f:
  vent_lines = [line.rstrip() for line in f]

# initialize points
lines = list()

# input parsing
for line in vent_lines:
  pts = line.split('->')
  x1, y1 = map(lambda x: int(x), pts[0].split(","))
  x2, y2 = map(lambda x: int(x), pts[1].split(","))
  lines.append([x1, y1, x2, y2])

# determine grid size and construct grid
max_x = max([ll[0] for ll in lines] + [ll[2] for ll in lines])
max_y = max([ll[1] for ll in lines] + [ll[3] for ll in lines])
grid_size = (max_x + 1, max_y + 1)
grid = np.zeros(grid_size)

for i in range(len(lines)):
  x1, y1, x2, y2 = lines[i]
  miny, maxy = min(y1, y2), max(y1, y2)
  minx, maxx = min(x1, x2), max(x1, x2)

  for j in range(max(maxx-minx, maxy-miny)+1):
    sx, sy = sign(x2-x1), sign(y2-y1)
    grid[x1+sx*j][y1+sy*j] += 1

answer = sum(sum(grid >= 2))
print("Answer: %d" % answer)
