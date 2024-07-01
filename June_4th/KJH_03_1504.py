# 백준 1504. 특정한 최단 경로


# 특정한 조건을 가지는 최단 경로를 구하는 문제
# 이미 이동했던 정점/간선도 이동할 수 있으며,
# 1 부터 N까지 이동하는데, 마지막에 주어지는 두 정점도 반드시 지나야한다.
# 경로가 겹쳐도 상관없기때문에,
# 1 -> v1 -> v2 -> N 으로 가는 경로와,
# 1 -> v2 -> v1 -> N 으로 가는 경로 중 짧은 경로를 구함
# 강 경로는 다익스트라로 구현

import sys
from heapq import heappop, heappush
from collections import defaultdict


# 다익스트라로 풀이
def dijkstra(start):
    """
    :param start: 시작 노드
    :return: 시작 노드로부터 다른 모든 노드까지의 거리
    """
    # 거리를 (N+1)개의 무한대 값으로 초기화
    distances = [float('inf')] * (N+1)
    # 시작 정점부터 시작 정점까지의 거리는 0으로 초기화
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heappop(pq)

        if cur_dist > distances[cur_node]:
            continue

        for next_node, next_dist in graph[cur_node]:
            distance = cur_dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heappush(pq, (distance, next_node))

    return distances


# 정점 갯수 N, 간선 갯수 E 입력
N, E = map(int, input().split())

# 그래프를 인접 리스트로 저장
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1에서부터 다른 모든 정점까지의 최소 거리
dist_from_1 = dijkstra(1)
# v1에서부터 다른 모든 정점까지의 최소 거리
dist_from_v1 = dijkstra(v1)
# v2에서부터 다른 모든 정점까지의 최소 거리
dist_from_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N의 최소 거리
dist_1_v1_v2_N = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
# 1 -> v2 -> v1 -> N의 최소 거리
dist_1_v2_v1_N = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]
# 두 거리 중 최소 거리 출력
result = min(dist_1_v2_v1_N, dist_1_v1_v2_N)

if result < float('inf'):
    print(result)
else:
    print(-1)