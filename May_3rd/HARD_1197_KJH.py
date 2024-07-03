# 백준 1197. 최소 신장 트리
# 프림 알고리즘을 이용한 풀이
# 정점을 선택하고 정점에 연결된 간선을 (우선순위) 큐에 추가, 가장 작은 가중치의 간선을 선택해서 다음 정점으로 이동

from heapq import heappop, heappush

V, E = map(int, input().split())

# 노드의 수가 최대 10000개
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)

# 문제에 주어지는 간선의 수만큼 반복
for i in range(E):
    # 정점1, 정점2, 가중치 입력
    A, B, C = map(int, input().split())
    # 그래프 입력 (가중치, 정점) 순서로
    graph[A].append((C, B))
    graph[B].append((C, A))

q = [(0, 1)]    # 시작 정점은 임의로 1로 선정, (가중치, 정점)
total_cost = 0  # 최종 결과값으로 출력할 가중치

while q:
    cost, node = heappop(q)
    if not visited[node]:
        visited[node] = 1
        total_cost += cost
        for edge in graph[node]:    # 현재 정점에 연결된 간선 순회
            if not visited[edge[1]]:    # 방문하지 않은 정점인 경우
                heappush(q, edge)

print(total_cost)