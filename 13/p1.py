# https://adventofcode.com/2021/
# day 13, puzzle 1

import numpy as np


points = list()
instructions = list()

# parsing input
with open('input.txt') as f:
  for line in f:
    if line == "\n":
      continue
    elif line.startswith("fold"):
      direction, coordinate = line.rstrip().split(" ")[2].split("=")
      instructions.append([direction, int(coordinate)])
    else:
      points.append([int(v) for v in line.rstrip().split(",")])

# build initial paper
paper = np.zeros((max([x[1] for x in points])+1, max([x[0] for x in points])+1), dtype=int)
for x in points:
  paper[x[1], x[0]] = 1

for i in instructions:
  direction, coordinate = i[0], i[1]
  xmax, ymax = paper.shape

  if direction == 'y':
    top, bottom = paper[0:coordinate, 0:ymax], paper[coordinate+1:xmax, 0:ymax]
    new_bottom = np.zeros(top.shape)
    new_bottom[top.shape[0]-bottom.shape[0]:top.shape[0],0:ymax] = np.flip(bottom, axis=0)
    paper = top + new_bottom

  if direction == 'x':
    left, right = paper[0:xmax, 0:coordinate], paper[0:xmax, coordinate+1:ymax]
    new_right = np.zeros(left.shape)
    new_right[0:xmax, left.shape[1]-right.shape[1]:left.shape[1]] = np.flip(right, axis=1)
    paper = left + new_right

  break  # we only deal with the first one

nonzero = np.where(paper>0)
answer = len(nonzero[0])
print("Answer: %d" % answer)
