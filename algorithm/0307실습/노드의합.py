import sys
sys.stdin = open("노드의합_input.txt")

def printTree():
    for i in range(1, N+1):
        print("%2d %2d" % (i, tree[i][0]))

tc = int(input())
for T in range(tc):
    N, M, L = map(int, input().split())
    tree = [[0 for _ in range(1)] for _ in range(N + 2)]
    for i in range(M):
        node, num = map(int, input().split())
        tree[node][0] = num
    for i in range(int(N//2)):
        if N % 2 == 1:
            pos = N-(2*i)
            tree[int(pos//2)][0] = tree[pos][0] + tree[pos-1][0]
        else:
            pos = N-(2*i)
            tree[int(pos // 2)][0] = tree[pos][0] + tree[pos + 1][0]
    print("%s%d %d" % ('#', T+1, tree[L][0]))