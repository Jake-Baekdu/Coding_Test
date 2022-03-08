from collections import deque

city_num, road_num, k, start_city = map(int, input().split())
dist = [float('inf') for _ in range(city_num+1)]
roads = [[] for _ in range(city_num+1)]

for _ in range(road_num):
    a, b = map(int, input().split())
    roads[a].append(b)
    
dq = deque([(0, start_city)])
dist[start_city] = 0
while(dq):
    w, s = dq.popleft()
    
    if dist[s] < w:
        continue
    
    for i in roads[s]:
        if dist[i] > dist[s] + 1:
            dist[i] = dist[s] + 1
            dq.append((dist[i], i))
flag = False
for i in range(1, city_num+1):
    if dist[i] == k:
        print(i)
        flag = True
        
if flag == False:
    print(-1)
