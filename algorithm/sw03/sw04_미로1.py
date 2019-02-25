import sys
sys.stdin = open("sw04_미로1_input.txt")
testcases = 10

def dfs(x, y):
    dx = [-1, 1, 0 , 0] # 좌, 우, 하, 상
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[ny][nx] == 0: # 함수를 넣어서 갈 수 있는 것만 통과
            maze[ny][nx] = 9
            dfs(nx, ny)
        if maze[ny][nx] == 3:
            return 1
    return 0

for T in range(testcases):
    tc = input()
    maze = []
    for i in range(16):
        tmp = list(map(int, input().split()))
        maze.append(tmp)
    print(dfs(1, 1))
    # 출발점은 1,1 로 동일하고 가로는 x 세로는 y다.
    # 도착점은 3이며 통로는 0이다. 도착점을 찾지못하며 0반환 찾으면 1반환
    # 방문한 곳은 9를 넣어 방문표시를 하고 더이상 진행할수 없으면 진행할수있는 상태로 되돌아가야한다.
    # 시작점에서 상하좌우를 확인하여 '0' 인곳을 찾아 이동한다.
    # 상하좌우에 '0'이 없으면 그 전상황으로 돌아간다
    # 모든 상황에 '0'이 없으면 최종적으로 0을 반환한다.

