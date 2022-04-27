n,m=map(int, input().split())
r,c,d=map(int, input().split())
dr=[-1, 0, 1, 0]
dc=[0, 1, 0, -1]
wall=[list(map(int, input().split())) for _ in range(n)]
ans=1
wall[r][c]=2
while True:
    turn=0
    while turn < 4:
        d=(d+3)%4
        nr = r + dr[d]
        nc = c + dc[d]
        if wall[nr][nc] == 0:
            r=nr
            c=nc
            wall[r][c]=2
            ans+=1
            break
        turn+=1
    if turn == 4:
        nr=r+dr[(d+2)%4]
        nc=c+dc[(d+2)%4]
        if wall[nr][nc] == 1:
            break
        else:
            r=nr
            c=nc
print(ans)