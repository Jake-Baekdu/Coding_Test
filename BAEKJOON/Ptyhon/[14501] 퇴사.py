import sys
from collections import deque

n = int(input())
T, P = [0 for i in range(n)], [0 for i in range(n)]
for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
dp =[0 for i in range(n+1)]

for i in range(n-1, -1, -1):
    if T[i]+i <= n: # 날짜를 초과하지 않을 경우
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])