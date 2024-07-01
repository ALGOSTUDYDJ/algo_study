# 14502. 연구소


# 1. 벽 3개를 임의로 세운다.
# 2. 벽 3개를 세운 후 해당 구조에서의 안전 영역을 계산한다.
# 3. 안전 영역의 최댓값을 계산한다.

import copy

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 벽을 세우는 함수
def createWall(k):
    if k == 3:
        # 벽이 3개일 때 할 일
        bfs()
        return
    for i in range(N):
        for j in range(M):
            # 빈 자리이면
            if board[i][j] == 0:
                board[i][j] = 1 # 벽을 세움
                createWall(k+1) # 다음 벽을 세움
                board[i][j] = 0 # 벽을 허뭄

# 바이러스를 확산시키고 안전영역을 계산하는 함수
def bfs():
    global max_safe                     # 전역변수 지정
    boardc = copy.deepcopy(board)       # 여러 번 수행하기 위해 deepcopy
    q = []
    
    # 바이러스 위치 찾기
    for i in range(N):
        for j in range(M):
            if boardc[i][j] == 2:
                q.append((i, j))
    
    while q:
        new_q = []
        for t in q:                 # 큐를 순회하며
            for d in dirs:          # 사방에 대해 다음 확산 위치 탐색
                di = t[0] + d[0]
                dj = t[1] + d[1]
                # 유효범위 내이고 빈 공간인 경우(확산 가능하다면)
                if 0 <= di< N and 0 <= dj < M and boardc[di][dj] == 0:
                    boardc[di][dj] = 2      # 확산
                    new_q.append((di, dj))  # 다음 탐색 위치로 추가
        q = new_q
    
    # 안전 영역의 수 계산
    cnt = 0
    for i in range(N):
        for j in range(M):
            if boardc[i][j]:
                continue
            cnt += 1
    # 최댓값 갱신
    max_safe = max(cnt, max_safe)

N, M = map(int, input().split())    # 세로, 가로
board = [list(map(int, input().split())) for _ in range(N)] # 지도

max_safe = 0    # 안전영역의 최댓값
createWall(0)   # 벽을 세우고 해당 벽에서의 안전영역 최댓값 탐색
print(max_safe)