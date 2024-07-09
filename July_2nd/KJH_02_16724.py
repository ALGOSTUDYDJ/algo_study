# 백준 16724. 피리 부는 사나이
import sys

# Find - Union처럼 보드에서 UDLR 방향이 몇 개의 집합으로 나누어지는지를 구하는 문제
# 어떻게 구현할건가?
# 1. BFS로 한 번의 방문에 갈 수 있는 방향, 올 수 있는 방향에 있는 모든 칸을 처리한다
# 2. 한 번의 BFS마다 방문처리 (visited)와 cnt를 갱신시켜주고,
# 1000 * 1000 번의 반복이 종료되고 나면 cnt값을 출력한다.

def set_safe_zone(start_i, start_j):
    global visited

    # q에 현재 좌표를 넣고 반복
    q = [(start_i, start_j)]

    while q:
        i, j = q.pop()

        # 이미 방문처리가 된 경우 넘어감
        if visited[i][j]:
            continue

        # 방문처리
        visited[i][j] = True

        # 현재 바라보고 있는 방향이 빈 칸이 아니면, 해당 칸을 방문처리해주기 위해 경로 q에 추가
        dir = pipes[i][j]
        ni, nj = i + dirs[dir][0], j + dirs[dir][1]

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            q.append((ni, nj))

        # 4방향을 순회하면서, 해당 방향에 있는 배열값이 현재 위치로 올 수 있는 방향이면 경로에 추가
        for d in dirs:
            # pi, pj는 i, j로 올 수 있는 4방향의 후보
            pi, pj = i + dirs[d][0], j + dirs[d][1]

            # 해당 방향이 배열에 들어오는 값이면,
            if 0 <= pi < N and 0 <= pj < M and not visited[pi][pj]:
                # 해당 방향에 있는 배열의 방향값이 (i, j)를 가리키는지 검사
                pd = dirs[pipes[pi][pj]]
                if i == pi + pd[0] and j == pj + pd[1]:
                    q.append((pi, pj))


# 방향 벡터 선언
dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

N, M = map(int, sys.stdin.readline().split())
visited = [[False] * M for _ in range(N)]
pipes = [sys.stdin.readline() for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            set_safe_zone(i, j)
            cnt += 1

print(cnt)