# https://adventofcode.com/2021/
# day 1, puzzle 1

with open('input.txt') as f:
  depths = [int(line.rstrip()) for line in f]

data = depths  # using depths as data
deeper = map(lambda i: 1 if data[i-1] < data[i] else 0, range(1, len(data)))
answer = sum(deeper)
print('Answer: %d' % answer)
