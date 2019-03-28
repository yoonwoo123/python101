def perm(n, k):
    if n == k:
        print(a)
    else:
        for i in range(k, n): # k = depth, n = 찾고자 하는 갯수
            a[i], a[k] = a[k], a[i]
            perm(n, k+1) # depth =  k+1
            a[i], a[k] = a[k], a[i] # 원래 값으로 복귀
flag = 0
a = [1, 2, 4, 7, 8, 3, 5, 6, 9]
perm(9, 0)
k = 0
n = 9