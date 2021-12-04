# https://adventofcode.com/2021/
# day 4, puzzle 1

import numpy as np
import math

with open('input.txt') as f:
  bingo = [line.rstrip() for line in f]

board_size = 5
# get the sequence of numbers called
numbers = list(map(lambda x: int(x), bingo[0].split(",")))
# get the number of boards in the file
num_boards = int((len(bingo)-1) / (board_size+1))

winning_board = ()
best_iteration = math.inf

for i in range(num_boards):
  strrd = [" ".join(bingo[2+(board_size+1)*i+x].lstrip(" ").split()).split() for x in range(board_size)]
  board = np.array(strrd, dtype=np.int)

  for x in range(len(numbers)):
    found = np.where(board == numbers[x])
    if found[0].size:
      board[found] = '-1'

    # determining winning conditions
    colsum = np.sum(board < 0, axis=0)  # sum by columns
    colwin = np.where(colsum == board_size)
    rowsum = np.sum(board < 0, axis=1)  # sum by rows
    rowwin = np.where(rowsum == board_size)

    if colwin[0].size or rowwin[0].size:
      if x < best_iteration:
        winning_board = board
        best_iteration = x
      break

winning_value = np.sum(np.where(winning_board > 0, winning_board, 0))
answer = numbers[best_iteration] * winning_value

print("Answer: %d" % answer)
