import sys
sys.stdin = open('숫자근_input.txt')


def numroot(numbers):
    global sum
    sum = 0
    for num in numbers: # 숫자근 함수
        sum += int(num)
    return sum

testcases = int(input())
root = [] # 숫자근의 합
origin = []
idx = []
test = []
# 함수로 만들어서 쉽게만들자.
for i in range(testcases):
    sum = 0
    N = int(input())
    # test.append(N)
    # print(test)
    origin.append(N) # 답을 출력하기 위한 origin 배열

    numbers = list(str(N))

    # print(len(numbers))

    numroot(numbers)
# 큰 숫자를 몫과 나머지로 나눠줄 수 있다.
    if len(list(str(sum))) == 1: # 숫자근의 합이 나오고 그 idx를 저장한다.
        # print(sum)
        root.append(sum)
        idx.append(i)
    if len(list(str(sum))) > 1:
        while len(list(str(sum))) != 1: # 길이가 1이 아니라면 다시돌리자
            numroot(list(str(sum)))
        # print(sum)
        root.append(sum)
        idx.append(i)
my_max = -1
b_max = -1
pri = []
stu = []

if root.count(max(root)) > 1: # 맥스가 여러개면 그 중 가장 작은수를 출력한다.
    for x in range(len(root)):
        if root[x] == max(root):
            pri.append(x)
    # print(pri)
    for y in pri:
        stu.append(origin[y])
    print(min(map(int, stu)))
else:

    pri = 0
    for x in range(len(root)): # 숫자근의 합이 가장큰 값의 idx를 구한다.
        if my_max < root[x]:
            my_max = root[x]
            pri = x

    # print(max(root))
    print(origin[idx[pri]]) # 답 그 가장큰 idx위치를 가진 origin을 출력
