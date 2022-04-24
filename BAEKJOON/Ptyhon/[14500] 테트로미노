import sys
from copy import deepcopy


x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(x)]

blocks = [[(0,0), (0,1), (0,2), (0,3)], # blue
[(0,0), (1,0), (2,0), (3,0)], 
[(0,0), (0,1), (1,0), (1,1)], # yello
[(0,0), (1,0), (2,0), (2,1)], # orange
[(0,0), (0,1), (0,2), (-1,2)],
[(0,0), (0,1), (1,1), (2,1)],
[(0,0), (0,1), (0,2), (1,0)],
[(0,0), (0,1), (-1,1), (-2,1)],
[(0,0), (1,0), (1,1), (1,2)],
[(0,0), (0,1), (1,0), (2,0)],
[(0,0), (0,1), (0,2), (1,2)],
[(0,0), (1,0), (1,1), (2,1)], # green
[(0,0), (0,1), (-1,1), (-1,2)],
[(0,0), (-1,0), (-1,1), (-2,1)],
[(0,0), (0,1), (1,1), (1,2)],
[(0,0), (0,1), (0,2), (1,1)], # purple
[(0,0), (0,1), (-1,1), (1,1)],
[(0,0), (0,1), (0,2), (-1,1)],
[(0,0), (0,1), (-1,0), (1,0)],
]

ans = 0

for sx in range(x):
    for sy in range(y):
        for block in blocks:
            tmp = 0
            for wx, wy in block:
                nx = sx + wx
                ny = sy + wy
                if nx < 0 or nx >= x or ny < 0 or ny >= y:
                    continue
                tmp += board[nx][ny]
            ans = max(ans, tmp)
                
print(ans)    
    