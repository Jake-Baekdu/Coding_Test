import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
direction = {
    (0,1) : [(-1,0), (1,0)],
    (1,0) : [(0,1), (0,-1)],
    (0,-1) : [(1,0), (-1,0)],
    (-1,0) : [(0,-1), (0,1)]
    }
    
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 'A'

L = int(sys.stdin.readline())
moveInfo = deque([0 for _ in range(L)])
for i in range(L):
    tmp = list(input().split())
    moveInfo[i] = [int(tmp[0]), tmp[1]]
    
time, direct = [0, (0,1)]
nowX, nowY = 0,0 
snakeBody = deque([[0,0]])
tail = snakeBody.popleft()
endFlag = False
while(True):
    if endFlag:
        break
    if moveInfo:
        checkTime, checkDirect = moveInfo.popleft()
    while(True):
        time += 1
        nowX += direct[0]
        nowY += direct[1]
        if nowX < 0 or nowX >= N or nowY < 0 or nowY >= N:
            endFlag = True
            break
        if [nowX, nowY] in snakeBody or [nowX, nowY] == tail:
            endFlag = True
            break
        
        snakeBody.append([nowX, nowY])
        if board[nowX][nowY] != 'A':
            tail = snakeBody.popleft()
        else:
            board[nowX][nowY] = 0
            
        
        if time == checkTime:
            if checkDirect == 'L':
                direct = direction[direct][0]
            else:
                direct = direction[direct][1]
            break
        
print(time)
        
        
        
        