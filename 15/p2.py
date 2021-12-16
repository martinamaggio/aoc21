# https://adventofcode.com/2021/
# day 15, puzzle 2

import numpy as np
from heapq import heappop, heappush

# parsing input
with open('input.txt') as f:
  risk_levels = [line.rstrip() for line in f]

rows = len(risk_levels)
cols = len(risk_levels[0])
base_risk = np.zeros((rows, cols), dtype=int)

for rr in range(rows):
  for cc in range(cols):
    base_risk[rr, cc] = int(risk_levels[rr][cc])

# constructing large input
repeat = 5
risk = np.zeros((rows*repeat, cols*repeat))
for ir in range(repeat):
  for ic in range(repeat):
    risk[ir*rows : ir*rows+rows, ic*cols : ic*cols+cols] = \
      np.mod(base_risk+ir+ic-1, 9) + 1

exploring = [(0, 0, 0)]
visited = np.zeros(risk.shape)
maxr, maxc = risk.shape[0]-1, risk.shape[1]-1

while True:
  value, r, c = heappop(exploring)
  if visited[r,c]:
    continue
  if (r, c) == (maxr, maxc):
    print("Answer: %d" % value)
    break
  visited[r,c] = True
  for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
    if maxr >= nr >= 0 <= nc <= maxc:
      heappush(exploring, (value+risk[nr,nc], nr, nc))
