import sys
sys.stdin = open("원안의사각형_input.txt")

R = int(input())
cnt=0
for i in range(1, R+1):
    for j in range(1, R+1):
        if R*R >= i*i + j*j:
            cnt+=1
print(cnt*4)
