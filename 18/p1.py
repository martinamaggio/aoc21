import math

with open("input.txt") as f:
  lines = [line.rstrip() for line in f]


class Pair:

  def __init__(self, l, r):
    self.left = l
    self.right = r
    self.parent = None
    self.set_children()
    self.isright = False
    self.isleft = False

  def __repr__(self):
    return "<" + str(self.left) + "," + str(self.right) + ">"

  def set_children(self):
    self.left.parent = self
    self.right.parent = self
    self.left.isleft, self.left.isright = True, False
    self.right.isleft, self.right.isright = False, True

  def rewrite(self, side, element):
    if side == 'r':
      self.right = element
      self.right.parent, self.right.isleft, self.right.isright = self, False, True
      self.right.set_children()
    if side == 'l':
      self.left = element
      self.left.parent, self.left.isleft, self.left.isright = self, True, False
      self.left.set_children()

  def get_leftof(self):
    if self.parent is None: return None
    elif self.isright: return self.parent.left
    else: return self.parent.get_leftof()

  def get_rightof(self):
    if self.parent is None: return None
    elif self.isleft: return self.parent.right
    else: return self.parent.get_rightof()

  def magnitude(self):
    return 3 * self.left.magnitude() + 2 * self.right.magnitude()

  def split(self, caller=None, side='x'):
    return self.left.split(self, 'l') or self.right.split(self, 'r')

  def add_left(self, v): self.left.add_left(v)
  def add_right(self, v): self.right.add_right(v)

  def explode(self, depth=0):

    if depth < 3:
      return self.left.explode(depth+1) or self.right.explode(depth+1)

    if depth >= 3:  # if I have a pair I'll have to explode

      if isinstance(self.left, Pair):
        l, r = self.left.left.v, self.left.right.v  # save values
        self.left = Number(0, self, True, False)  # overwriting with a left number zero
        self.right.add_left(r)
        if self.get_leftof() is not None:
          self.get_leftof().add_right(l)
        return True

      elif isinstance(self.right, Pair):
        l, r = self.right.left.v, self.right.right.v
        self.right = Number(0, self, False, True)
        self.left.add_right(l)
        if self.get_rightof() is not None:
          self.get_rightof().add_left(r)
        return True

      else:
        return False


class Number:
  def __init__(self, v, parent=None, isleft=False, isright=False):
    self.v = v
    self.parent = parent
    self.isright = isright
    self.isleft = isleft

  def __repr__(self):
    return str(self.v)

  def split(self, caller, side):
    if self.v < 10: return False
    else:
      caller.rewrite(side, Pair(Number(math.floor(self.v / 2)), Number(math.ceil(self.v / 2))))
      return True

  def add_left(self, v): self.v += v
  def add_right(self, v): self.v += v
  def magnitude(self): return self.v
  def explode(self, depth=0): pass


def parse_number(n):
  if isinstance(n, list):
    return Pair(parse_number(n[0]), parse_number(n[1]))
  else:
    return Number(n)


def reduce(x):
  while True:
    if x.explode():
      pass
    elif x.split():
      pass
    else: break  # I tried both and neither worked, I am done


result = None
for ll in lines:
  if result is None:  # first number
    result = parse_number(eval(ll))
  else:  # perform the sum
    number = parse_number(eval(ll))
    result = Pair(result, number)
    reduce(result)

answer = result.magnitude()
print("Answer: %d" % answer)
