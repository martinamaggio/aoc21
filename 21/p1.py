# https://adventofcode.com/2021/
# day 21, puzzle 1

with open("input.txt") as file:
  p1 = int(file.readline().split("Player 1 starting position: ")[1])
  p2 = int(file.readline().split("Player 2 starting position: ")[1])

p = [p1, p2]  # positions
s = [0, 0]  # scores


def play(p, s=[0,0], t=0, r=0, d=0):
  if s[0] >= 1000 or s[1] >= 1000:
    return s, r
  else:
    v = [(d + x - 1) % 100 + 1 for x in [1, 2, 3]]
    r += 3  # keep number of rolls
    p[t] = (p[t] + sum(v) - 1) % 10 + 1
    s[t] += p[t]
    return play(p, s, 1 if t == 0 else 0, r, d+3)


s, r = play(p)
answer = min(s)*r
print("Answer: %d" % answer)

