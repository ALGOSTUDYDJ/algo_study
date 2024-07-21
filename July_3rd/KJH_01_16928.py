import sys
from collections import deque

# 뱀 사다리 게임
# 시작점 "1" 부터 "100"까지 사다리 및 뱀을 타면서 가는 게임
# 가장 빠른 횟수를 구하는 문제로, BFS로 풀이한다.
# 각 지점에서 주사위 숫자인 1 ~ 6번만큼의 동작을 하면서, 저장되는 결과값은 보드에 미리 저장한 값으로 저장한다.
# BFS이므로 deque 자료구조를 활용한다.

N, M = map(int, input().split())

board = [int(i) for i in range(101)]

# 사다리 입력
for _ in range(N + M):
    start, end = map(int, sys.stdin.readline().split())
    board[start] = end

# 우선순위 큐, BFS로 풀이하기 위해 100부터 시작
visited = [0] * 101

start = (1, 0)
dq = deque([start])

min_result = 100

while dq:
    cur, cur_depth = dq.popleft()

    if cur == 100:
        min_result = min(min_result, cur_depth)
        break

    if visited[cur] and cur_depth >= visited[cur]:
        continue

    visited[cur] = cur_depth

    # 1에서 6까지 순회하면서, 해당
    for i in range(1, 7):
        next_num = cur + i
        if cur + i <= 100:
            temp = board[cur + i]

            dq.append((temp, cur_depth + 1))

print(min_result)