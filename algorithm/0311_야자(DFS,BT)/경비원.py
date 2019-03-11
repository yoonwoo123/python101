import sys
sys.stdin = open("경비원_input.txt")

w, h = map(int, input().split())
mart = int(input())
for i in range(mart):
    comp_meter = list(map(int, input().split()))
dong_cm = list(map(int, input().split()))