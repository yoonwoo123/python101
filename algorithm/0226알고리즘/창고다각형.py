import sys
sys.stdin = open('창고다각형_input.txt')

heights = []
N = int(input())

table = []
for i in range(1000): # 1000 X 1000 테이블
    table.append([0]*1000)

for i in range(N):
    L, H = map(int, input().split())
    heights.append(H)
    max(heights)

print(max(heights))
print(heights)
    # 창고의 최소 총면적을 구해야한다.
    # 테이블에 1로 표시해서 합으로 구해보자
    # 물이 고이지 않아야 하기 때문에 크고 작고 크고는 나올수 없다. 즉
    # 최대점을 한번 찍으면 그것보다 높은건 나오지않고 내려오기만한다.
    # 최종기둥을 빼고 양옆만 생각해보자.
