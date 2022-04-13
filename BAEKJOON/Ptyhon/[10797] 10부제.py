n = input()
cars = list(input().split())

ans = 0
for c in cars:
    if c[-1] == n:
        ans += 1
        
print(ans)