A, B, C, D = 1, 10, 100, 1000

answer = 0
answer += A * 7  # A from row 3 to leftmost corner
answer += B * 2  # B from row 2 to corridor one right
answer += A * 5  # A from row 2 to leftmost corner -1
answer += B * 3  # B from corridor to in
answer += C * 2  # C from row 4 to rightmost corner -1
answer += B * 7  # B from row 4 to row 2
answer += D * 6  # D from row 3 to row 4
answer += C * 5  # C from corridor to row 3
answer += D * 8  # D from row 1 to row 4
answer += C * 7  # C from row 1 to row 3
answer += A * 3  # A from leftmost corner -1 to row 1
answer += A * 3  # A from leftmost corner to row 1

print(answer)