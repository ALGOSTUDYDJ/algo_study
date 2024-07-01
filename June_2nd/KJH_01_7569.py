# 7569. 토마토


# 익은 토마트는 인접한 익지 않은 토마토에 영향을 줌
# 토마토가 전부 익기 위해 최소 며칠이 걸리는지 -> BFS로 풀이
from collections import deque

# 방향은 M, N, H 순으로 위 아래 왼쪽 오른쪽 앞 뒤 여섯 방향 -> MNH 거꾸로 해야함
# dirs = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)]
# 방향은 H, N, M 순으로 위 아래 왼쪽 오른쪽 앞 뒤 여섯 방향
dirs = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

# 입력 M, N, H
M, N, H = map(int, input().split())
# 3차원 배열 초기화
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 썩은 토마토
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방문처리 배열
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

q = deque([])

# 초기 조건 확인
# 3차원 배열을 순회하며 1이면 deque에 추가후 방문 처리, -1이면 그냥 방문 처리
# 0의 갯수를 계속 추적해준다
cnt_zero = 0
cnt_one = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            cur = tomatoes[i][j][k]
            if cur == 1:
                q.append((i, j, k, 0))
                visited[i][j][k] = True
                cnt_one += 1
            elif cur == -1:
                visited[i][j][k] = True
            else:
                cnt_zero += 1

# 0이 없으면
if cnt_zero == 0:
    q = []
    # 1이 한 개라도 있을 때 0 출력 후 반복 종료
    if cnt_one:
        print(0)
    # 전부 -1이면 -1 출력 후 반복 종료
    else:
        print(-1)
else:
    # deque 순회
    while q:
        cur = q.popleft()

        for d in dirs:
            ni = cur[0] + d[0]
            nj = cur[1] + d[1]
            nk = cur[2] + d[2]
            next_day = cur[3] + 1
            # print(ni, nj, nk)
            # 방문처리를 안한 리스트 값은 0밖에 없으므로, 방문처리가 안됐으면 반드시 안익은 토마토
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not visited[ni][nj][nk]:
                # 안익은 토마토가 발견되면 deque의 바로 다음 순서로 push
                visited[ni][nj][nk] = True
                q.append((ni, nj, nk, next_day))
                # 안익은 토마토 방문을 완료하면 바로 cnt_zero를 삭제해줌
                cnt_zero -= 1

        if not cnt_zero:
            print(q[-1][3])
            break
    else:
        print(-1)