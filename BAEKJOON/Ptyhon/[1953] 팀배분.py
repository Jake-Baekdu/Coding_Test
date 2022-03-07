from collections import deque


flag = 'blue'

def dfs(v):
    flag = 0
    dq = deque()
    dq.append(v)
    visited[v] = True
    
    while dq:
        for n in dq:
            teams[flag].append(n)
        for _ in range(len(dq)):
            v = dq.popleft()
            for nv in hate_list[v]:
                if not visited[nv]:
                    visited[nv] = True
                    dq.append(nv)
        flag ^= 1

        
n = int(input())
teams= [[], []]

hate_list = [[] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    hate_list[i+1] = tmp[1:]

visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

print(len(teams[0]))
print(*sorted(teams[0]))
    
print(len(teams[1]))
print(*sorted(teams[1]))