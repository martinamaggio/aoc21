# https://adventofcode.com/2021/
# day 10, puzzle 1

def score_character(c):
  if c == ')': return 3
  if c == ']': return 57
  if c == '}': return 1197
  if c == '>': return 25137


with open('input.txt') as f:
  delimiters_lines = [line.rstrip() for line in f]

answer = 0

for line in delimiters_lines:

  stack = []

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
        answer += score_character(character)
        break

print("Answer: %d" % answer)
