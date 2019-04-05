def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d " % (T[q]), end = "")
    print()
def H(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:
        return
    else:
        T[r-1] = A[n-1]
        H(n, r-1, q) # 중복조합
        # H(n-1, r - 1, q) # 조합
        H(n-1, r, q)

A = [1, 2, 3, 4]
T = [0] * 3

H(4, 3, 3)