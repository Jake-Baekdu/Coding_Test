n, m = map(int, input().split())
x, y, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
move_direction = [(-1,0), (0,1), (1,0), (0,-1)] #북, 동, 남, 서

ans = 1
board[x][y] = 2
while True:
    cnt = 0
    while cnt < 4:
        D = (D+3)%4
        tx = x + move_direction[D][0]
        ty = y + move_direction[D][1]
        
        if board[tx][ty] == 0:
            x = tx
            y = ty
            board[x][y] = 2
            ans += 1
            break
        cnt += 1
       
    if cnt == 4 :
        tx = x + move_direction[(D+2)%4][0]
        ty = y + move_direction[(D+2)%4][1]
        if board[tx][ty] == 1:
            break
        else:
            x = tx
            y = ty
print(ans)
