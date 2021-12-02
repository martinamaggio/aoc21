# https://adventofcode.com/2021/
# day 2, puzzle 2

with open('input.txt') as f:
  commands = [line.rstrip() for line in f]

depth = 0
position = 0
aim = 0

for i in range(len(commands)):
  c = commands[i].split(" ")
  if c[0] == 'forward':
    position += int(c[1])
    depth += aim*int(c[1])
  elif c[0] == 'down':
    aim += int(c[1])
  elif c[0] == 'up':
    aim -= int(c[1])

answer = depth * position

print('Depth: %d, Position: %d' % (depth, position))
print('Answer: %d' % answer)
