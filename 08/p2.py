# https://adventofcode.com/2021/
# day 8, puzzle 2

with open('input.txt') as f:
  segments_list = [line.rstrip() for line in f]

segments_input = list(map(lambda x: x.split('| ')[0], segments_list))
segments_output = list(map(lambda x: x.split('| ')[1], segments_list))
answer = 0

for i in range(len(segments_list)):

  input_values = segments_input[i].split(' ')
  output_values = segments_output[i].split(' ')

  # initialising segments to empty sets
  c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()

  # immediately identifying obvious segments
  c1 = set([c for c in list(filter(lambda x: len(x) == 2, input_values))[0]])
  c4 = set([c for c in list(filter(lambda x: len(x) == 4, input_values))[0]])
  c7 = set([c for c in list(filter(lambda x: len(x) == 3, input_values))[0]])
  c8 = set([c for c in list(filter(lambda x: len(x) == 7, input_values))[0]])

  # handling the 6-segments digits
  for j in input_values:
    segments = set([c for c in j])
    if len(segments) == 6:
      if   c4.issubset(segments):  c9 = segments
      elif c1.issubset(segments):  c0 = segments
      else:                        c6 = segments

  # the simplest way to handle the 5-segments is to have determined the 6-segments
  for j in input_values:
    segments = set([c for c in j])
    if len(segments) == 5:
      if   c1.issubset(segments): c3 = segments
      elif segments.issubset(c9): c5 = segments
      else:                       c2 = segments

  identified_segments = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]

  # now we have inferred all the segments-set for the numbers
  pos0001_digit = list(filter(lambda x: set([c for c in output_values[3]]) == identified_segments[x], range(10)))[0]
  pos0010_digit = list(filter(lambda x: set([c for c in output_values[2]]) == identified_segments[x], range(10)))[0]
  pos0100_digit = list(filter(lambda x: set([c for c in output_values[1]]) == identified_segments[x], range(10)))[0]
  pos1000_digit = list(filter(lambda x: set([c for c in output_values[0]]) == identified_segments[x], range(10)))[0]
  output_value = pos1000_digit * 1000 + pos0100_digit * 100 + pos0010_digit * 10 + pos0001_digit

  answer += output_value

print("Answer: %d" % answer)
