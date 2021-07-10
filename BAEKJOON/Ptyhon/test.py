from collections import deque
string = input()
boom = input()


def crop(T, A):
    dq = deque(T)
    
    N = "FRULA"
    while A in T:
        A_idx = T.find(A)
        dq = dq[:A_idx] + dq[A_idx + len(A):] 
            
    if len(T) == 0:
        return N
    else:
        return T

print(crop(string, boom))