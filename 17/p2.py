# https://adventofcode.com/2021/
# day 17, puzzle 2

x_min, x_max = 230, 283
y_min, y_max = -107, -57
target = (x_min, x_max, y_min, y_max)


def launch(vx, vy, target):

  p = 0, 0  # position
  v = vx, vy  # velocity
  x_min, x_max, y_min, y_max = target

  while True:

    p = p[0] + v[0], p[1] + v[1]
    v = 0 if v[0] == 0 else v[0] + (-1 if v[0] > 0 else 1), v[1] - 1

    if v[0] == 0 and not x_min <= p[0] <= x_max:
      return None  # cannot go further in x
    if p[0] > x_max:
      return None  # outside target area
    if p[1] < y_min:
      return None  # too deep

    if x_min <= p[0] <= x_max and y_min <= p[1] <= y_max:
      return v


answer = 0
for vx in range(-300, 300, 1):  # heuristic
  for vy in range(-300, 300, 1):

    if launch(vx, vy, target) is not None:
      answer += 1

print("Answer: %d" % answer)
