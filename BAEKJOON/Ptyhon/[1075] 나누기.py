import sys
from collections import deque
# input = "sys.stdin.readline"

a = int(input())
b = int(input())

tmp = int(a[:-2] + '00')

while(True):
    if tmp % b == 0:
        break
    tmp += 1

print(str(tmp)[-2:])