
import sys

S = set()
n = int(sys.stdin.readline())

for _ in range(n):
    commends = list(sys.stdin.readline().split())
    if len(commends) == 2:
        commend = commends[0]
        num = commends[1]
    else:
        commend = commends[0]
        
        
    if commend == 'add':
        S.add(num)
    elif commend == 'remove':
        if num in S:
            S.remove(num)
    elif commend == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif commend == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif commend == 'all':
        S = {n for n in range(1, 21)}
    elif commend == 'empty':
        S = set()
