# https://adventofcode.com/2021/
# day 10, puzzle 2

with open('input.txt') as f:
  delimiters_lines = [line.rstrip() for line in f]

incomplete_line_values = list()

for line in delimiters_lines:

  stack, line_value, discard = [], 0, False

  for character in line:

    if character in ['(', '[', '{', '<']:
      stack.append(character)

    else:
      last = stack.pop()
      if   last == '(' and character == ')': continue
      elif last == '[' and character == ']': continue
      elif last == '{' and character == '}': continue
      elif last == '<' and character == ">": continue
      else:
        discard = True
        break

  while not discard and stack:
    c = stack.pop()
    if c == '(': line_value = line_value * 5 + 1
    if c == '[': line_value = line_value * 5 + 2
    if c == '{': line_value = line_value * 5 + 3
    if c == '<': line_value = line_value * 5 + 4

  if line_value != 0:
    incomplete_line_values.append(line_value)

line_values = sorted(incomplete_line_values)
answer = line_values[int(len(line_values)/2)]

print("Answer: %d" % answer)
