from bisect import bisect

def min_max(a):
    m, n = 10**9, 1
    for x in a: m = min(m, x); n = max(n, x)
    return m, n

def main():
    input()
    arr = [int(x) for x in input().split()]
    x, y = min_max(arr)

    # All elements are the same
    if x == y:
        return 1

    # Actually more efficient than iterating once and appending to separate lists
    # (by design of the language constructs)
    m = [i for i, e in enumerate(arr) if e == x]
    n = [i for i, e in enumerate(arr) if e == y]
    del arr  # No longer required

    # Min and Max are different but each occur only once
    if len(m) == 1 == len(n):
        return abs(m[0] - n[0]) + 1

    # Better to iterate through the shorter array since it'll be in linear time
    p = min(m, n, key=len)
    q = n if p is m else m
    del m, n

    l = 5000
    for j in p:
        i = bisect(q, j)
        if i > 0:
            l = min(l, abs(j - q[i-1]) + 1)
        if i < len(q):
            l = min(l, abs(j - q[i]) + 1)
        if l == 2:  # Can't go any less
            return 2

    return l

print(main())
