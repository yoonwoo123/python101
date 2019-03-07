import sys
sys.stdin = open("workshop_사칙연산_input.txt")

def printTree():
    for i in range(1, N+1):
        print("%2d %2d %2d %2s" % (i, tree[i][0], tree[i][1], tree[i][2]))
# 읽어올때 중위연산 inorder
def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        res.append('(')
        res.append(tree[node][2])
        print(tree[node][2], end=" ")
        inorder(tree[node][1])

tc = 10
for T in range(tc):
    N = int(input())
    res = []
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    # 0 = left, 1 = right , 2 = 값 나중에 num은 int 꼭 씌워줘야함!!
    # operation을 나중에 계산해 줄때는 if '/' == operator 이런식으로 찾아서 계산해줘야함

    for i in range(N):
        data = input().split()
        if len(data) == 2:
            node, num = data
            tree[int(node)][2] = num
        elif len(data) == 4:
            node, operator, left, right = data
            tree[int(node)][0] = int(left)
            tree[int(node)][1] = int(right)
            tree[int(node)][2] = operator

    for i in range(int(N//2)):
        pos = N- 2*i
        parent = tree[int(pos//2)][2]
        if parent == '+':
            tree[int(pos // 2)][2] = int(tree[pos-1][2]) + int(tree[pos][2])
        elif parent == '-':
            tree[int(pos // 2)][2] = int(tree[pos-1][2]) - int(tree[pos][2])
        elif parent == '*':
            tree[int(pos // 2)][2] = int(int(tree[pos-1][2]) * int(tree[pos][2]))
        elif parent == '/':
            tree[int(pos // 2)][2] = int(int(tree[pos-1][2]) // int(tree[pos][2]))

    # inorder(1)
    # print()
    # print(res)
    printTree()
    print()