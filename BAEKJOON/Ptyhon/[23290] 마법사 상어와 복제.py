import copy

def move_fish():
    """
    물고기 이동
    1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 x 
    2. 45도 반시계 회전 후 이동. 이동 못하는 경우 그대로 
    :return:
    """
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    """
    상어 3칸 이동
    1. 제외되는 물고기 수가 많고 > 이동방법 사전순(백트래킹하면 자동으로 됨) 
    2. 이동한 곳을 저장 > 물고기 냄새가 됨  
    """
    global max_eat, shark, eat
    if dep == 3:   # 3번 이동한 경우 그만 
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가  
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)

#       ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    graph[x - 1][y - 1].append(d - 1)

shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    eat = list()
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(graph)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어이동 - 백트래킹
    dfs(shark[0], shark[1],0, 0, list())
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3   # 3번 돌아야 없어짐
    # 4. 냄새 사라짐 
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp[i][j]

# 물고기 수 구하기 
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])

print(answer)




# from collections import deque


# # def moveShark(_sx, _sy):
# #     dq = deque()
# #     dq.append([_sx, _sy, 0, 0, "", []])
# #     visited = [[0 for _ in range(5)] for _ in range(5)]
# #     move_shark = [0, (-1,0),(0,-1),(1,0),(0,1)]
    
# #     max_xy = [0, 0, 0, "", []] # fish, x, y, dictionary, move_memory
# #     while(dq):
# #         x, y, move_cnt, fish_cnt, dictional_num, move_memory = dq.popleft()
# #         if visited[x][y] == 1:
# #             continue
# #         visited[x][y] = 1
        
# #         if move_cnt == 3: # three move done
# #             if max_xy[0] < fish_cnt: 
# #                 max_xy = [fish_cnt, x, y, dictional_num, move_memory]
# #             elif max_xy[0] == fish_cnt:
# #                 if max_xy[3] > dictional_num:
# #                     max_xy = [fish_cnt, x, y, dictional_num, move_memory]
# #             continue

# #         for i in range(1,5):
# #             tx = x + move_shark[i][0]
# #             ty = y + move_shark[i][1]
# #             if 0 < tx < 5 and 0 < ty < 5:
# #                 if visited[tx][ty] == 1:
# #                     continue
# #                 tmp_cnt = fish_cnt + len(board[tx][ty])
# #                 dq.append([tx, ty, move_cnt+1, tmp_cnt, dictional_num+str(i), move_memory + [tx, ty]])
                

# #     for i in range(0, len(max_xy[4]), 2):
# #         tx = max_xy[4][i]
# #         ty = max_xy[4][i+1]
# #         if len(board[tx][ty])>0:
# #             board[tx][ty] = []
# #             fish_smell[tx][ty].add(practice_cnt)
# #     board[_sx][_sy].remove(-1)
# #     board[max_xy[1]][max_xy[2]].append(-1)
# #     return max_xy[1], max_xy[2]
    
# move_shark = [(-1,0),(0,-1),(1,0),(0,1)]
# max_eat = -1
# eat_path = []
# def moveShark(_sx, _sy, cnt, eat_cnt, visit):
#     global sx, sy
#     if cnt == 3:
#         if max_eat < eat_cnt:
#             max_eat = eat_cnt
#             sx, sy = _sx, _sy
#             eat_path = visit[:]
#     for wx, wy in move_shark:
#         tx = sx + wx
#         ty = sy + wy
#         if 0 < tx < 5 and 0 < ty < 5:
#             if (tx, ty) not in visit:
#                 visit.append((tx, ty))
#                 moveShark(tx, ty, cnt + 1, eat_cnt + len(board[tx][ty]), visit)
#                 visit.pop()
#             else:
#                 moveShark(tx, ty, cnt + 1, eat_cnt, visit)

    


              
              
# # START
# M, S = map(int, input().split())
# board = [[[] for _ in range(4+1)] for _ in range(4+1)]
# fish_smell = [[0 for _ in range(4+1)] for _ in range(4+1)]
# fish = deque()

# for _ in range(M):
#     x, y, d = map(int, input().split())
#     board[x][y].append(d-1)
#     fish.append([x, y, d-1])
    
# sx, sy = map(int, input().split())


# #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
# move_xy = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

# practice_cnt = 0
# for _ in range(S):
#     practice_cnt += 1
    
#     #duplicate fishes
#     tmp_fishes = []
#     for i in range(1, 5):
#         for j in range(1, 5):
#             if board[i][j] and -1 not in board[i][j]:
#                 for k in board[i][j]:
#                     tmp_fishes.append([i,j,k])
    
#     # move fishes
#     for fx, fy, fd in fish:
#         cnt = 0
#         flag = False
#         while cnt < 8:
#             td = (fd-cnt)%8
#             tx = fx + move_xy[td][0]
#             ty = fy + move_xy[td][1]
#             if 0 < tx <= 4 and 0 < ty <= 4:
#                 if fish_smell[tx][ty] > 0 or (tx == sx and ty == sy):
#                     cnt += 1
#                     continue
#                 flag = True
#                 board[tx][ty].append(td)
#                 break
#             else:
#                 cnt += 1
#                 continue
#         if flag:
#             board[fx][fy].remove(fd)

#     moveShark(sx, sy, 0, 0, [])

#     for x, y in eat_path:
#         if board[x][y]:
#             board[x][y] = []
#             fish_smell[x][y] = 3
        
#     for i in range(1,5):
#         for j in range(1,5):
#             if fish_smell[i][j]:
#                 fish_smell[i][j] -= 1

    
#     for i, j, d in tmp_fishes:
#         board[i][j].append(d)
    
# ans = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if len(board[i][j]) > 0 :
#             ans += len(board[i][j])

# print(ans)
                
                
                
                
                
                
                
                
    

