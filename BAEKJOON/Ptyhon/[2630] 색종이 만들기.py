import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

        
white, blue = 0, 0
def main(x, y, n):
    global white, blue
    
    color = board[x][y]
    flag = True
    
    for i in range(x, x+n):
        if flag == False:
            break
        
        for j in range(y, y+n):
            if color != board[i][j]:
                flag = False
                main(x, y, n//2)
                main(x+n//2, y, n//2)
                main(x, y+n//2, n//2)
                main(x+n//2, y+n//2, n//2)
                break
    
    if flag:
        if color:
            blue += 1
        else:
            white += 1
            
main(0, 0, N)
print(white)
print(blue)
    