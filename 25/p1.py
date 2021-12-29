from copy import copy
import numpy as np

with open("input.txt") as f:
  lines = [l.rstrip() for l in f]

ms = mh, mw = len(lines), len(lines[0])
m = np.zeros(ms, dtype=int)

for r in range(mh):
  for c in range(mw):
    if lines[r][c] == ">": m[r, c] = 1
    if lines[r][c] == "v": m[r, c] = 2

steps = 1
moved = True

while moved:

  moved = False

  ir_r, ir_c = np.where(m == 1)
  id_r, id_c = np.where(m == 2)
  nr, nd = len(ir_r), len(id_r)

  nm = copy(m)

  # first the ones moving right
  for i in range(nr):
    pr, pc = ir_r[i], ir_c[i]
    nc = (pc + 1) % mw
    if m[pr, nc] == 0:
      nm[pr, nc], nm[pr, pc] = 1, 0
      moved = True

  m = copy(nm)

  # then the ones moving down
  for i in range(nd):
    pr, pc = id_r[i], id_c[i]
    nr = (pr + 1) % mh
    if m[nr, pc] == 0:
      nm[nr, pc], nm[pr, pc] = 2, 0
      moved = True

  m = nm

  if not moved:
    break
  else:
    steps += 1

answer = steps
print("Answer: %d" % answer)
