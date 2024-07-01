# 1303. 전쟁-전투


# 1. 좌상단부터 순회하며 인접한 병사들의 수를 계산한다.
# 2. 인접한 병사들의 수를 계산한 후 팀에 맞추어 전력을 계산한다.
# 3. 아군과 적군의 전력을 출력한다.

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 방향 배열
def bfs(start, color):     # 탐색 시작 지점, 해당 팀 색깔
    q = [start]
    cnt = 1                 # 병사의 수
    visited[i][j] = 1       # 방문 표시
    while q:
        new_q = []
        for t in q:
            for d in dirs:
                dr = d[0] + t[0]
                dc = d[1] + t[1]
                # 유효범위이면서 방문하지 않은 점이며
                if 0<=dr<M and 0<=dc<N and visited[dr][dc] == 0:
                    if board[dr][dc] == color:  # 같은 팀이면
                        cnt += 1                # 같은 편 인원 증가
                        visited[dr][dc] = 1     # 방문 표시
                        new_q.append((dr, dc))  # 다음 탐색 위치로 추가
        q = new_q   # 새 탐색 위치 배열 추가
    
    return cnt

N, M = map(int, input().split())    # 가로 크기, 세로 크기

# 병사들의 배치
board = [list(map(str, input())) for _ in range(M)] # M개의 줄

visited = [[0 for _ in range(N)] for _ in range(M)] # 방문 여부

blue = 0    # 적군
white = 0   # 아군

for i in range(M):
    for j in range(N):
        if visited[i][j]:   # 확인한 병사이면 통과
            continue
        num = bfs((i, j), board[i][j])  # 같은 팀 병사의 수 확인
        # 각 팀에 맞추어 전력 증가
        if board[i][j] == 'B':
            blue += num**2
        else:
            white += num**2

print(white, blue)