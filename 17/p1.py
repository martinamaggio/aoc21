# https://adventofcode.com/2021/
# day 17, puzzle 1

x_min, x_max = 230, 283
y_min, y_max = -107, -57
target = (x_min, x_max, y_min, y_max)


def launch(vx, vy, target):

  p = 0, 0  # initial position
  v = vx, vy  # velocity
  x_min, x_max, y_min, y_max = target

  h_max = 0
  while True:

    p = p[0] + v[0], p[1] + v[1]
    v = 0 if v[0] == 0 else v[0] + (-1 if v[0] > 0 else 1), v[1] - 1
    h_max = p[1] if p[1] > h_max else h_max

    if v[0] == 0 and not x_min <= p[0] <= x_max:
      return -1  # cannot go further in x
    if p[0] > x_max:
      return -1  # outside target area
    if p[1] < y_min:
      return -1  # too deep

    if x_min <= p[0] <= x_max and y_min <= p[1] <= y_max:
      return h_max


answer = 0
for vx in range(-300, 300, 1):  # heuristic
  for vy in range(-300, 300, 1):

    current = launch(vx, vy, target)
    if current > answer:
      answer = current

print("Answer: %d" % answer)
