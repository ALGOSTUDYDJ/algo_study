#1647. 도시 분할 계획
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# 간선으 수를 순회해야함
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

max_connected_edge = 0
total_weight = 0

q = [(0, 1)]

while q:
    weight, node = heappop(q)
    # 이미 방문한 노드면 넘기기
    if visited[node]:
        continue
    else:
        # 방문 처리
        visited[node] = True
        # 이어진 길 중 최대값을 저장 (계속 갱신)
        max_connected_edge = max(weight, max_connected_edge)
        # 유지비 총합 계산
        total_weight += weight
        
        # 그래프에서 현재 노드의 값을 순회
        for edge in graph[node]:
            # 미방문한 노드면 heappush
            if not visited[edge[1]]:
                heappush(q, edge)

print(total_weight - max_connected_edge)