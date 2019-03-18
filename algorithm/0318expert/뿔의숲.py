import sys
sys.stdin = open("뿔의숲_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())
    N-