import sys
sys.stdin = open("subtree_input.txt")

def printTree():
    for i in range(1, E+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

def preorder(node): # 1을 집어넣음
    global cnt
    if node != 0: # node 값이 0이 아니면 들어간다.
        cnt += 1
        preorder(tree[node][0]) # 1의 left
        preorder(tree[node][1]) # 1의 right


tc = int(input())
for T in range(tc):
    cnt = 0
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]

    for i in range(E):
        n1 = data[2*i]  # 부모
        n2 = data[2*i + 1]  # 자식
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1 # n2의 부모는 n1

    # printTree()
    preorder(N)
    print("%s%d %d" % ('#', T+1, cnt))
