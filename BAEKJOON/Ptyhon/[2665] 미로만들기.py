import heapq

n = int(input())

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(input())
    
dist = [[float("INF") for _ in range(n)] for _ in range(n)]

def dijkstra():
        move_xy = [(1,0),(0,1),(-1,0),(0,-1)]
        hq = []
        
        start = 0
        if board[0][0] == '0':
            start = 1
            
        heapq.heappush(hq, (start, 0, 0))
        dist[0][0] = start
        
        while(hq):
            w, x, y = heapq.heappop(hq)
            
            if x == n-1 and y == n-1:
                break
            
            for tx, ty in move_xy:
                nx = x + tx
                ny = y + ty
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = dist[x][y]
                    
                    if board[nx][ny] == '0':
                        new_cost += 1
                        
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(hq, (new_cost, nx, ny))

dijkstra()
print(dist[n-1][n-1])
    