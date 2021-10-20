from bisect import bisect, insort

def min_max(a):
    m, n = 10**9, 1
    for x in a: m = min(m, x); n = max(n, x)
    return m, n

def main():
    input()
    arr = [int(x) for x in input().split()]
    x, y = min_max(arr)
    if x == y:
        return 1

    m = [i for i, e in enumerate(arr) if e == x]
    n = [i for i, e in enumerate(arr) if e == y]
    if len(m) == 1 == len(n):
        return abs(m[0] - n[0]) + 1
    del arr
    p = min(m, n, key=len)
    q = n if p is m else m

    l = 5000
    for j in p:
        i = bisect(q, j)
        if i > 0:
            l = min(l, abs(j - q[i-1]) + 1)
        if i < len(q):
            l = min(l, abs(j - q[i]) + 1)
        if l == 2:
            return 2

    return l

print(main())
