# https://adventofcode.com/2021/
# day 21, puzzle 2

with open("input.txt") as file:
  p0 = int(file.readline().split("Player 1 starting position: ")[1])
  p1 = int(file.readline().split("Player 2 starting position: ")[1])


def play(p0, p1, s0=0, s1=0, memory={}):
  memory_key = (p0, p1, s0, s1)
  if memory_key in memory:
      return memory[memory_key]

  w0, w1 = 0, 0
  v = [(r1, r2, r3) for r3 in [1, 2, 3] for r2 in [1, 2, 3] for r1 in [1, 2, 3]]
  for r in v:
    p0_new = (p0 + sum(r) - 1) % 10 + 1
    s0_new = s0 + p0_new
    if s0_new >= 21:
      w0 += 1
    else:
      dw1, dw0 = play(p1, p0_new, s1, s0_new)
      w0, w1 = w0 + dw0, w1 + dw1
  memory[memory_key] = w0, w1
  return w0, w1


w = play(p0, p1)
answer = max(w)
print("Answer: %d" % answer)
