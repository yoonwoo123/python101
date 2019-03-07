import sys
sys.stdin = open("도약_input.txt")

N = int(input())
leafs = []
for i in range(N):
    leafs.append(int(input()))
leafs = sorted(leafs)
cnt = 0
for pos in range(len(leafs)-2):
    jump = 0
    for jmp in range(pos+1, len(leafs)):
        if jump == 1:
            if term <= leafs[jmp] - leafs[pos] <= term * 2:
                cnt += 1
                continue
            else:
                continue
        jump += 1
        term = leafs[jmp] - leafs[pos]
        leafs[pos] = leafs[jmp] # 개구리 현재 위치를 뛴위치로변경
print(cnt)