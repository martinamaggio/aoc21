# https://adventofcode.com/2021/
# day 20, puzzle 2

import numpy as np


def get_pixel(i, r, c):
  binary = "".join(["".join([str(i[x, y]) for y in [c-1, c, c+1]]) for x in [r-1, r, r+1]])
  pixel = int(binary, 2)
  return pixel


def enhancement_step(i, a, pad_size):
  i = np.pad(i, pad_size)
  newi = np.zeros(i.shape, dtype=int)
  for r in range(1, i.shape[0]-1):
    for c in range(1, i.shape[1]-1):
      newi[r, c] = a[get_pixel(i, r, c)]
  return newi[1:-1,1:-1]  # removing outmost line


with open("input.txt") as f:
  lines = [l.rstrip() for l in f]

algorithm = [1 if i == "#" else 0 for i in lines[0]]

s = rows, cols = len(lines) - 2, len(lines[2])
i = np.zeros(s, dtype=int)
for r in range(i.shape[0]):
  for c in range(i.shape[1]):
    i[r, c] = 1 if lines[2+r][c] == "#" else 0

pad_size = 5
for _ in range(25):
  for _ in range(2):
    i = enhancement_step(i, algorithm, pad_size)
  i = i[pad_size:-pad_size, pad_size:-pad_size]

answer = np.sum(i)
print("Answer: %d" % answer)
