# https://adventofcode.com/2021/
# day 16, puzzle 2

import functools

with open('input.txt') as f:
  t = [line.rstrip() for line in f]
received = list("".join([bin(int(c, 16))[2:].zfill(4) for c in t[0]]))


def split(message):

  def to_int(num, base=10):
    return int("".join(num), base)

  # parse initial stuff
  version = to_int(message[0:3], 2)
  type_id = to_int(message[3:6], 2)
  message[:] = message[6:]

  # deal with number packets
  if type_id == 4:

    number = []
    while True:

      first_position = message[0]  # remove character in position 0
      message[:] = message[1:]
      number += message[:4]
      message[:] = message[4:]
      if first_position == "0":
        break
    value = to_int(number, 2)

    return (version, type_id, value)

  # deal with operator packets
  else:

    sub_packets = list()
    length_type_id = message[0]
    message[:] = message[1:]

    if length_type_id == '0':  # we have a message length

      msg_length = to_int(message[:15], 2)
      message[:] = message[15:]
      current_msg = message[:msg_length]
      message[:] = message[msg_length:]
      while current_msg:
        sub_packets.append(split(current_msg))

    else:  # we have a number of packets

      num_packets = to_int(message[:11], 2)
      message[:] = message[11:]
      for _ in range(num_packets):
        sub_packets.append(split(message))

    return (version, type_id, sub_packets)


def value(x):
  if   x[1] == 0: return sum([value(p) for p in x[2]])
  elif x[1] == 1: return functools.reduce(lambda i, j: i*j, [value(p) for p in x[2]])
  elif x[1] == 2: return min([value(i) for i in x[2]])
  elif x[1] == 3: return max([value(i) for i in x[2]])
  elif x[1] == 4: return x[2]
  elif x[1] == 5: return 1 if value(x[2][0]) > value(x[2][1]) else 0
  elif x[1] == 6: return 1 if value(x[2][0]) < value(x[2][1]) else 0
  elif x[1] == 7: return 1 if value(x[2][0]) == value(x[2][1]) else 0


packets = [split(received)]
packets_values = [value(p) for p in packets]
answer = sum(packets_values)
print("Answer: %d" % answer)
