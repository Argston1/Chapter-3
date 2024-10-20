import sys
sys.setrecursionlimit(99999)

m = {}

def f(n):
    if n in m:
        return m[n]
    if n == 0: return 0
    if n == 1:
        return 1
    m[n] = f(n - 1) + f(n - 2)
    return m[n]

print(f(int(input())))