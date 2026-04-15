def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dorbro(n):
    n += 2
    return n