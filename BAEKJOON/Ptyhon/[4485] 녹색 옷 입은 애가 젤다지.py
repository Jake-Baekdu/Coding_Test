import heapq
count = 1
while(True):
    n = int(input())
    
    if n == 0:
        break
    
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    
    distance = [[float('INF')] * n for _ in range(n)]
    
    def dijkstra():
        move_xy = [(1,0),(0,1),(-1,0),(0,-1)]
        hq = []
        heapq.heappush(hq, (arr[0][0], 0, 0))
        distance[0][0] = arr[0][0]
        
        while(hq):
            w, x, y = heapq.heappop(hq)
            if x == n-1 and y == n-1:
                print("Problem {}: {}".format(count, distance[x][y]))
                break

            
            for tx, ty in move_xy:
                nx = x + tx
                ny = y + ty
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = distance[x][y] + arr[nx][ny]
                    if new_cost < distance[nx][ny]:
                        distance[nx][ny] = new_cost
                        heapq.heappush(hq, (new_cost, nx, ny))

    dijkstra()
    count += 1
    
    
    
    