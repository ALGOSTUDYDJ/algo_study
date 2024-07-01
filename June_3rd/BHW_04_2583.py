# 2583. 영역 구하기


# 1. K개 직사각형을 색칠한다.
# 2. 전체 영역을 순회하며 색칠되지 않은 영역이 있는 경우 해당 영역을 시작으로 분리된 해당 영역을 칠한다.
# 3. 2의 과정을 모든 영역이 색칠될 때까지 반복할 경우 2의 횟수가 영역의 수가 된다.
# 4. 각 영역의 넓이는 해당 영역을 탐색하며 색칠한 점의 수와 같다.

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우

def bfs(start):         # 분리된 영역을 색칠하는 함수
    q = [start]         # 시작점 enque
    board[start[0]][start[1]] = 1           # 방문처리
    area = 1
    while q:
        new_q = []      # 다음 깊이의 배열
        for t in q:
            for d in dirs:                  # 상하좌우를 탐색하며
                dr = t[0] + d[0]
                dc = t[1] + d[1]
                if 0 <= dr < M and 0 <= dc < N: # 유효범위 내에서
                    if board[dr][dc] == 0:      # 미방문 점이 있으면 enque
                        area += 1               # 면적도 증가
                        board[dr][dc] = 1       # 방문처리
                        new_q.append((dr, dc))
            q = new_q                           # 다음 깊이로 갱신
    
    return area

M, N, K = map(int, input().split()) # M행, N열, K개의 직사각형

board = [[0 for _ in range(N)] for _ in range(M)]   # M행 N열의 직사각형

# K개의 직사각형에 대해 영역을 칠한다.
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())      # 좌하단 꼭짓점 좌표, 우상단 꼭짓점 좌표
    for r in range(y1, y2):         # 상하
        for c in range(x1, x2):     # 좌우
            board[r][c] = 1

cnt = 0                     # 영역의 수
areas = []

for r in range(M):
    for c in range(N):
        if board[r][c]:     # 색칠된 영역이면 미방문
            continue
        cnt += 1            # 색칠되지 않은 경우 영역의 수 증가 및 해당 영역 색칠
        areas.append(bfs((r, c)))

areas.sort()        # 넓이 오름차순 정렬
print(cnt)
print(*areas)