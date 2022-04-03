import sys
from collections import deque
# input = "sys.stdin.readline"

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0,0,0,0,0,0]
def turn(_dir):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if _dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif _dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif _dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
       
       
n, m, x, y, k = map(int ,input().split())
board = [list(map(int ,input().split())) for _ in range(n)]
order = list(map(int ,input().split()))

for w in order:
    x = x + dx[w-1]
    y = y + dy[w-1]
    
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[w-1]
        y -= dy[w-1]
        continue

    turn(w)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])

