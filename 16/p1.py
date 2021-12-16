# https://adventofcode.com/2021/
# day 16, puzzle 1

with open('input.txt') as f:
  t = [line.rstrip() for line in f]
received = list("".join([bin(int(c, 16))[2:].zfill(4) for c in t[0]]))


def split(message, packets=[]):

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

    packets.append(version)
    return packets

  # deal with operator packets
  else:

    sub_packets = []
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

    packets.append(version)
    return packets


versions = split(received)
answer = sum(versions)
print("Answer: %d" % answer)
