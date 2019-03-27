def perm(n, k):
    if n == k:
        print(a)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]
flag = 0
a = [1, 2, 4, 7, 8, 3]
# perm(6, 0)
k = 0
n = 2
cli = [[1,2], [4,7]]

cli[0], cli[1] = cli[1], cli[0]

print(cli)