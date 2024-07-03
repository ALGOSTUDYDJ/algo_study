import sys
from heapq import heappop, heappush

# i -> x -> i 의 최대값을 구하는 문제입니다.
# 중복이 없는 유향 그래프 형식으로 반드시 이어지는 길로 입력이 주어집니다.
# 플로이드-워셜 알고리즘의 경우 시간복잡도가 O(N^3)이므로, 입력이 최대 1000이면 1,000,000,000 (10억)으로 시간초과 문제
# 따라서 다익스트라로 풀이하며,
# x -> i는 일반적인 다익스트라 알고리즘으로 방문처리 하면서 각 노드까지의 거리를 저장
# i -> x는 역방향의 그래프 값을 가중치로 거꾸로 다익스트라를 돌림 (총 두 번의 다익스트라) O(Elog(V) * 2)
# i -> x 와 x -> i 의 합 중 최대값으로 결과값을 출력합니다.

# N, M, X 입력
N, M, X = map(int, sys.stdin.readline().split())

# 방문 정보 리스트 초기화
# visitied : X에서 i로 가는 최단 경로
visited = [False] * N
distances = [float('inf')] * N
# visited_reverse : i에서 X로 가는 최단 경로
visited_reverse = [False] * N
distances_reverse = [float('inf')] * N

# 그래프 양방향을 구분해야하므로 인접그래프 형식으로 저장
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start-1][end-1] = weight

# 정방향 다익스트라
hq = [(0, X-1)]
while hq:
    cur_weight, cur_node = heappop(hq)

    # 이미 방문한 노드면 넘어감
    if visited[cur_node]:
        continue

    # 방문한 적 없는 노드면 현재 노드에 현재 거리를 저장
    distances[cur_node] = cur_weight
    visited[cur_node] = True

    # 현재 노드에 연결돼 있는 마을을 순회하며, 연결되어 있는데 방문한 적이 없는 마을은 heappush로 경로 추가
    for i in range(N):
        next_node = i
        next_weight = graph[cur_node][i]
        if next_weight and not visited[next_node]:
            heappush(hq, (cur_weight + next_weight, next_node))

# 역방향 다익스트라
hq = [(0, X-1)]
while hq:
    cur_weight, cur_node = heappop(hq)

    # 이미 방문한 노드면 넘어감
    if visited_reverse[cur_node]:
        continue

    # 방문한 적 없는 노드면 현재 노드에 현재 거리를 저장
    distances_reverse[cur_node] = cur_weight
    visited_reverse[cur_node] = True

    # 현재 노드에 연결돼 있는 마을을 순회하며, 연결되어 있는데 방문한 적이 없는 마을은 heappush로 경로 추가
    for i in range(N):
        next_node = i
        next_weight = graph[i][cur_node]
        if next_weight and not visited_reverse[next_node]:
            heappush(hq, (cur_weight + next_weight, next_node))

# 두 다익스트라의 결과를 함께 순회하면서 합이 가장 큰 경우를 출력함
farthest = 0
for i in range(N):
    distance_i = distances[i] + distances_reverse[i]
    farthest = max(farthest, distance_i)

print(farthest)

