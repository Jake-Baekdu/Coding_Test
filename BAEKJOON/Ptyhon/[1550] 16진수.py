import sys

S = 0b0

for _ in range(int(sys.stdin.readline())):
    commends = list(sys.stdin.readline().split())

    if commends[0] == 'add':
        S = S | (0b1 << int(commends[1]))
    elif commends[0] == 'remove':
        if (S & (0b1 << int(commends[1]))):
            S = S & ~(0b1 << int(commends[1]))
    elif commends[0] == 'check':
        if (S & (0b1 << int(commends[1]))):
            print(1)
        else:
            print(0)
    elif commends[0] == 'toggle':
        S = S ^ (0b1 << int(commends[1]))
            
    elif commends[0] == 'all':
        S = 0b111111111111111111111
    elif commends[0] == 'empty':
        S = 0b0
