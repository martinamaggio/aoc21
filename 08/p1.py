# https://adventofcode.com/2021/
# day 8, puzzle 1

with open('input.txt') as f:
  segments = [line.rstrip() for line in f]

segments_output = list(map(lambda x: x.split('| ')[1], segments))
answer = 0

for i in segments_output:
  output_values = i.split(' ')
  count = list(map(lambda x: 1 if len(x) in [2, 3, 4, 7] else 0, output_values))
  answer += sum(count)

print("Answer: %d" % answer)
