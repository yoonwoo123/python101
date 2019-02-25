import sys
sys.stdin = open("sw03_모음_input.txt")
testcases = int(input())
for T in range(testcases):
    bowel = ['a', 'e', 'i', 'o', 'u']
    res = []
    word = list(input())
    for char in word:
        if char not in bowel:
            res.append(char)
    print(f"#{T+1} {''.join(res)}")