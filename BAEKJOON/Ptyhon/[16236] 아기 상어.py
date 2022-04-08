import sys, copy
from collections import deque
import heapq

def find_fish(_time):
    dq = deque([[sx, sy, _time]])
    visited = [[0] * n for _ in range(n)]
    move_xy = [(-1,0), (0,-1), (0,1), (1,0)]
    visited[sx][sy] = 1
    temp = []

    while(dq):
        x, y, time = dq.popleft()
        
        for wx, wy in move_xy:
            nx = x + wx
            ny = y + wy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] > shark:
                    continue
                if 0 < board[nx][ny] < shark:
                    time += 1
                    temp.append([nx, ny, time])
                else:
                    visited[nx][ny] = 1
                    dq.append([nx, ny, time+1])
                    
    temp = sorted(temp, key = lambda x:(x[2], x[0], x[1]))
    if temp:
        return temp[0]
    else:
        return 0
            
if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    sx, sy = 0, 0 
    fishs = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                sx, sy = i, j
                board[i][j] = 0
            elif board[i][j] != 0:
                heapq.heappush(fishs, board[i][j])

    shark = 2
    time = 0
    eat_cnt = 0
    while(fishs):
        fish = heapq.heappop(fishs)
        if fish >= shark:
            break
        val = find_fish(time)
        if val == 0:
            break
        else:
            sx, sy, time = val

        board[sx][sy] = 0
        eat_cnt += 1
        if shark == eat_cnt:
            shark += 1
            eat_cnt = 0
    print(time)
