import sys
sys.stdin = open("이진힙_input.txt")

def printTree():
    for i in range(1, len(numbers)+1):
        print("%2d %2d" % (i, tree[i][0]))

tc = int(input())
for T in range(tc):
    res = 0
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [[0 for _ in range(1)] for _ in range(len(numbers)+1)]
    tree[1][0] = numbers[0] # root값은 미리 넣어둔다.

    for i in range(1, len(numbers)):
        pos = i + 1
        tree[pos][0] = numbers[i] # 값을 삽입

        while numbers[i] < tree[int(pos//2)][0]: # 삽입값 < 부모값
            numbers[i], tree[int(pos//2)][0] = tree[int(pos//2)][0], numbers[i] # python의 swap 부모-자식을 스왑
            pos = int(pos // 2)
    pos = len(numbers)
    while pos != 0:
        res += tree[int(pos//2)][0]
        pos = int(pos // 2)
    print("%s%d %d" % ('#', T+1, res))
    printTree()
    print()
