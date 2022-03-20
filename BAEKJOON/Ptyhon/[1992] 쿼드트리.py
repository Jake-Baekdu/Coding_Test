import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    tmp = list(input())
    board[i] = list(map(int, tmp[:-1]))
ans = ""

def main(x, y, n):
    global ans
    color = board[x][y]
    flag = True
    for i in range(x, x+n):
        if flag == False:
            break
        
        for j in range(y, y+n):
            if color != board[i][j]:
                ans += '('
                flag = False
                main(x, y, n//2)
                main(x, y+n//2, n//2)
                main(x+n//2, y, n//2)
                main(x+n//2, y+n//2, n//2)
                ans += ')'
                break
    
    if flag:
        if color:
            ans += '1'
        else:
            ans += '0'
        
    
    
    
main(0,0,N)
print(ans)
    