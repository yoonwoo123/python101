import sys
sys.stdin = open("원안의사각형_input.txt")

R = int(input())
s = int(R // 1.414)

int((R // 1.414)**2) +

while h > 1:
    w = s + 1
    h = s - 1
    total += 2*(w * h - s * h)
    s = w
    h = w
# if w < h:
#     total += (w * h - s * w)
# 사분면을 4개로 나눠서 생각한다치고 사분면 1개 * 4 해주자

