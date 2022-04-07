import sys
# input = "sys.stdin.readline"

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    cnt = 1
    for i in range(1, W+1):
        for j in range(1, H+1):
            if cnt == N:
                if i >= 10:
                    ans = str(j) +str(i)
                else:
                    ans = str(j) + '0' +str(i)
                print(ans)
            cnt += 1
