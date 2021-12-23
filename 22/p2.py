# https://adventofcode.com/2021/
# day 22, puzzle 2

def intersect(x1, x2, ox1, ox2):
  return x1 <= ox1 <= x2 or x1 <= ox2 <= x2 or ox1 <= x1 <= ox2 or ox1 <= x2 <= ox2


def intersection(c1a, c2a, c1b, c2b):
  c1 = c1a if c1b < c1a else c1b
  c2 = c2a if c2a < c2b else c2b
  return c1, c2


class cuboid:
  def __init__(self, x1, x2, y1, y2, z1, z2) -> None:
    self.x1, self.x2 = x1, x2
    self.y1, self.y2 = y1, y2
    self.z1, self.z2 = z1, z2
    self.off = []

  def is_intersecting(self, other):
    return (intersect(self.x1, self.x2, other.x1, other.x2) and
            intersect(self.y1, self.y2, other.y1, other.y2) and
            intersect(self.z1, self.z2, other.z1, other.z2))

  def minus(self, other):
    if self.is_intersecting(other):
      x = intersection(self.x1, self.x2, other.x1, other.x2)
      y = intersection(self.y1, self.y2, other.y1, other.y2)
      z = intersection(self.z1, self.z2, other.z1, other.z2)

      for o in self.off:
          o.minus(other)
      self.off.append(cuboid(x[0], x[1], y[0], y[1], z[0], z[1]))

  def volume(self):
    return (self.x2 - self.x1 + 1) * \
           (self.y2 - self.y1 + 1) * \
           (self.z2 - self.z1 + 1) - \
           sum([c.volume() for c in self.off])


cuboids = []

with open("input.txt") as f:
  steps = [l.rstrip() for l in f]

for i in steps:
  v = 1 if i.split(" ")[0] == "on" else 0
  x1, x2 = [int(n) for n in i.split(" ")[1].split(",")[0].split("x=")[1].split("..")]
  y1, y2 = [int(n) for n in i.split(" ")[1].split(",")[1].split("y=")[1].split("..")]
  z1, z2 = [int(n) for n in i.split(" ")[1].split(",")[2].split("z=")[1].split("..")]

  n_cube = cuboid(x1, x2, y1, y2, z1, z2)
  for c in cuboids:
    c.minus(n_cube)
  if v:
    cuboids.append(n_cube)

answer = sum([c.volume() for c in cuboids])
print("Answer: %d" % answer)
