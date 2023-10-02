## Problem 21 (not working)
def d(a):
    arr = []
    c = 0
    b = 2
    while True:
        c = a/b
        if c.is_integer():
            if arr.__contains__(b):
                break
            arr.append(b)
            arr.append(c)
        b = b+1
    return sum(arr)+1

def solve(k):
    arr2 = []
    a2 = k-1
    while True:
        print(a2)
        b2 = d(a2)
        if d(b2) == b2:
            arr2.append(a2)
            arr2.append(b2)
        a2=a2-1
        if a2==1:
            return sum(arr2)

print(solve(10000))