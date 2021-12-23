# https://adventofcode.com/2021/
# day 22, puzzle 1

import itertools
import numpy

with open("input.txt") as f:
  steps = [l.rstrip() for l in f]

s = []

for i in steps:
  v = 1 if i.split(" ")[0] == "on" else 0
  x1, x2 = [int(n) for n in i.split(" ")[1].split(",")[0].split("x=")[1].split("..")]
  y1, y2 = [int(n) for n in i.split(" ")[1].split(",")[1].split("y=")[1].split("..")]
  z1, z2 = [int(n) for n in i.split(" ")[1].split(",")[2].split("z=")[1].split("..")]
  if x1 >= -50 and x2 <= 50 and y1 >= -50 and y2 <= 50 and z1 >= -50 and z2 <= 50:
    s.append((v, x1, x2, y1, y2, z1, z2))


hc = numpy.zeros((101, 101, 101))

for i in s:
  v, x1, x2, y1, y2, z1, z2 = i
  l = [range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)]
  u = itertools.product(*l)
  for x, y, z in u:
    hc[x+50, y+50, z+50] = v

answer = numpy.count_nonzero(hc)
print("Answer: %d" % answer)
