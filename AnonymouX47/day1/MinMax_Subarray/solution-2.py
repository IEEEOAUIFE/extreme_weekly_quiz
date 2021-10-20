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

    j = k = l = 5000
    changed = False
    for i, e in enumerate(arr):
        if e == x:
            j = i; changed = True
        elif e == y:
            k = i; changed = True
        if changed:
            l = min(l, abs(j - k) + 1)
            changed = False
        if l == 2:
            return l

    return l

print(main())
