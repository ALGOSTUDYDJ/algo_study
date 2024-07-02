# 1197. 최소 스패닝 트리


# 1. 간선을 가중치 순으로 정렬
# 2. 가중치가 낮은 순서대로 순회하면서
# 3. 해당 경로의 두 정점을 모두 방문한 경우는 경로로 추가하지 않음
# 4. 모든 정점을 방문하는 순간까지 반복(V-1개 간선)

import sys
from queue import PriorityQueue

# 조상을 찾는 함수
def find(cld):
    # 내가 조상이면 반환
    if cld == parent[cld]:
        return cld
    # 조상의 조상을 찾아서 반환
    parent[cld] = find(parent[cld])
    return parent[cld]

# 두 정점을 연결시키는 함수
def union(a, b):
    # a의 조상과 b의 조상을 받아와서
    a = find(a)
    b = find(b)
    # 같은 조상이 아니면 a의 조상쪽으로 연결
    if a!=b:
        parent[b] = a

V, E = map(int, sys.stdin.readline().split())
pq = PriorityQueue()
parent = [i for i in range(V+1)]

# 가중치 순으로 우선순위 큐에 집어 넣음
for _ in range(E):
    fr, to, cost = map(int, sys.stdin.readline().split())
    pq.put((cost, fr, to))

cnt = 0     # 간선의 수
total = 0   # 가중치의 합
# 간선의 수가 V-1일 때까지
while cnt < V - 1:
    # 하나씩 꺼내서
    cost, fr, to = pq.get()
    if find(fr) != find(to):    # 조상이 같지 않으면(연결이 안 된 점이면)
        union(fr, to)           # 연결
        total += cost           # 해당 비용 추가
        cnt += 1                # 횟수 추가

print(total)                    # 가중치 합 출력