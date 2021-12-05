# https://adventofcode.com/2021/
# day 5, puzzle 1
import numpy as np

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
grid_size = (max_x+1, max_y+1)
grid = np.zeros(grid_size)

for i in range(len(lines)):
  x1, y1, x2, y2 = lines[i]
  miny, maxy = min(y1, y2), max(y1, y2)
  minx, maxx = min(x1, x2), max(x1, x2)
  if x1 == x2:
    for j in range(miny, maxy+1):
      grid[x1][j] += 1
  if y1 == y2:
    for j in range(minx, maxx+1):
      grid[j][y1] += 1

answer = sum(sum(grid >= 2))
print("Answer: %d" % answer)
