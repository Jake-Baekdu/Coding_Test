import sys
# input = "sys.stdin.readline"

a = input()
b = int(input())

tmp = int(a[:-2] + '00')

while(True):
    if tmp % b == 0:
        break
    tmp += 1

print(str(tmp)[-2:])