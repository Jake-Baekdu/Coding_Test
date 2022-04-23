import sys
from copy import deepcopy


n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for i in range(n):
    if a[i] <= b:
        ans += 1
        continue
    
    a[i] -= b
    ans += 1
    
    ans += a[i]//c
    if a[i]%c != 0:
        ans += 1
        
print(ans)