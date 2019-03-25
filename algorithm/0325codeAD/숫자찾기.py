import sys, bisect
sys.stdin = open('숫자찾기_input.txt')

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid + 1 # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0

N = int(input())
numbers = list(map(int, input().split()))
T = int(input())
numbersT = list(map(int, input().split()))

for target in numbersT:
    print(binary_search(target, numbers))