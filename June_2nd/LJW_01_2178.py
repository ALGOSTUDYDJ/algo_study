from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 곳 이 있고 길이 있는경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
# 이동할 위치 추가 및 기록
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    # 최단 거리
    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

graph[0][0] = 1

print(bfs(0, 0))