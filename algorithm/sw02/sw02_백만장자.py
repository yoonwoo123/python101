import sys
sys.stdin = open('sw02_백만장자_input.txt')

testcases = int(input())
for T in range(testcases):
    N = int(input())

    nums = list(map(int,(input().split())))

    print(nums)