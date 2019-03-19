import sys
sys.stdin = open("최대성적표_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, K = map(int, input().split())