import sys
import heapq
# input = "sys.stdin.readline"
import datetime


board = [list(input()) for _ in range(8)]

ans = 0
flag = 'W'
for i in range(8):
    if i%2 == 0:
        flag = 'W'
    else:
        flag = 'B'
    for j in range(8):
        if flag == 'W' and board[i][j] == 'F':
            ans += 1
        if flag == 'W':
            flag = 'B'
        else:
            flag = 'W'
print(ans)