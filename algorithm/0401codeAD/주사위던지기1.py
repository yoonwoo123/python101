import sys
sys.stdin = open("주사위던지기1_input.txt")
# M1 = 중복순열 구조 :
# M2 = 중복조합 구조 : 조합은 내 앞은 볼 필요 없으므로 start를 들고간다
                     # 그래서 start 부터 시작하면 됨
# M3 = 순열 구조
# M4 가 있다면 조합 구조 : start + 1 부터 시작하면됨
N, M = map(int, input().split())

def DFS(no, start):
