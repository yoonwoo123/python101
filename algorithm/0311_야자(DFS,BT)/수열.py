import sys
sys.stdin = open("수열_input.txt")

N = int(input())
line = list(map(int, input().split()))
cnt = []
h_res = 1
high = []
l_res = 1
low = []
for i in range(N):
    if len(cnt) == 0:
        cnt.append(line[i])
        continue
    elif line[i] > cnt[-1]:
        cnt.append(line[i])
        h_res += 1
        high.append(h_res)
        l_res = 1

    elif line[i] < cnt[-1]:
        cnt.append(line[i])
        l_res += 1
        low.append(l_res)
        h_res = 1

    else: # 둘이 같을때
        cnt.append(line[i])
        h_res += 1
        l_res += 1
        high.append(h_res)
        low.append(l_res)
if max(high) > max(low):
    print(max(high))
else:
    print(max(low))

