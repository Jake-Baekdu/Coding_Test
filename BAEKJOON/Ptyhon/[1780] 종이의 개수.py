import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

n_1 = 0
n_0 = 0
n_m1 = 0

def main(x, y, n):
    global n_1, n_0, n_m1
    num = board[x][y]
    flag = True
    for i in range(x, x+n):
        if flag == False:
            break
        for j in range(y, y+n):
            if num != board[i][j]:
                flag = False
                main(x, y, n//3)
                main(x, y+ n//3, n//3)
                main(x, y+ 2*(n//3), n//3)
                main(x+n//3, y, n//3)
                main(x+n//3, y+ n//3, n//3)
                main(x+n//3, y+ 2*(n//3), n//3)
                main(x+2*(n//3), y, n//3)
                main(x+2*(n//3), y+ n//3, n//3)
                main(x+2*(n//3), y+ 2*(n//3), n//3)
                break
        
    if flag:
        if num == -1:
            n_m1 += 1
        elif num == 0:
            n_0 += 1
        else:
            n_1 += 1

main(0, 0, N)
print(n_m1)
print(n_0)
print(n_1)
