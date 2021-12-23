# https://adventofcode.com/2021/
# day 19, puzzle 1

import copy

with open("input.txt") as f:
  data = f.read()

sd = []  # scanner data

for s in data.split("\n\n"):
  s = s.splitlines()[1:]
  sd.append({tuple(map(int, i.split(","))) for i in s})


# vector difference
def vsub(x, y): return tuple(i-j for i, j in zip(x, y))

def rotations(s):
  s = copy.deepcopy(s)
  k = []
  for _ in range(4):
    for _ in range(4):
      k.append(s)
      s = {(z, y, -x) for x, y, z in s}
    k.append({(y, -x, z) for x, y, z in s})
    k.append({(-y, x, z) for x, y, z in s})
    s = {(x, z, -y) for x, y, z in s}
  return k

def intersect(bp, sd):
  for csd in rotations(sd):
    for b in bp:
      for bt in csd:
        o = vsub(bt, b)  # calculate offset between b and bt
        bc = {vsub(bt, o) for bt in csd}  # possible beacon positions converted
        if len(bp & bc) >= 12: return o, bc
  return None, []


# initialisation
bp = set(sd[0])  # beacon positions
sp = [(0, 0, 0)]  # scanner positions
rsd = sd[1:]  # the remaining scanner data

while rsd:
  csd = rsd[0]  # current scanner data, get the first position
  ocsd, pcsd = intersect(bp, csd)
  if pcsd:  # found intersection: offset and positions
    bp |= pcsd  # introduce converted beacon positions in the set
    sp.append(ocsd)
    rsd.pop(0)
  else:
    rsd.append(rsd.pop(0))  # could not find it yet

answer = len(bp)
print("Answer: %d" % answer)
