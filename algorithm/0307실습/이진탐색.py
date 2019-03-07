import sys
sys.stdin = open("이진탐색_input.txt")

def printTree():
    for i in range(1, N+1):
        print("%2d %2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2], tree[i][3]))

def inorder(node):
    global cnt
    if node != 0:
        inorder(tree[node][0])
        # print(node, end=" ")
        tree[node][3] = cnt
        cnt += 1
        inorder(tree[node][1])

tc = int(input())
for T in range(tc):
    cnt = 1
    N = int(input())
    tree = [[0 for _ in range(4)] for _ in range(N+1)]

    for i in range(1, int((N+1)//2)+1): # i = 1, 2, 3, 4, 5, 6
        tree[i][2] = int(i // 2)
        tree[i][0] = i * 2
        if i * 2 == N:
            break
        tree[i][1] = i * 2 + 1
        if i * 2 + 1 == N:
            break

    inorder(1)
    # print()
    # printTree()
    # print()
    print("%s%d %d %d" % ('#', T+1, tree[1][3], tree[int(N // 2)][3]))