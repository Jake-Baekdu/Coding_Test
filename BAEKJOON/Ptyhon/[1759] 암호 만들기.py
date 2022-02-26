import itertools

L, C = map(int, input().split())
strings = list(input().split())
gathers = {'a','e','i','o','u'}
strings.sort()

combi = list(itertools.combinations(strings, L))

for cb in combi:
    c = set(cb) - gathers
    if len(c) >= 2 and L-len(c) >= 1:
        print(''.join(cb))
