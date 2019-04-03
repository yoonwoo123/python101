import sys
sys.stdin = open('연습2_input.txt')

# 16 진수 > 2진수 > 10진수

asc = [[0, 0, 0, 0], # 0
       [0, 0, 0, 1], # 1
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]] # F

def aToh(c):
    if c <= '9':return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = input()
# print(arr)
for i in range(len(arr)):
    makeT(aToh(arr[i]))
print(t)
n = 0
for i in range(len(t)):
    n = n * 2 + t[i]
    if i % 7 == 6:
        print(n, end=", ")
        n = 0
if i % 7 != 6:
    print(n)