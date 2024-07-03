# 1647. 도시 분할 계획
# 2개의 최소 스패닝 트리의 유지비 합이 최소가 되도록


# 1. 유지비 합이 최소가 되는 2개의 최소 스패닝 트리를 만들기 위한 방법은
# 2. 전체를 연결하는 최소 스패닝 트리에서 비용이 가장 비싼 경로를 제거하는 것
# 3. 경로가 낮은 비용 순으로 순회하며 해당 경로가 아니면 두 집 간 통행이 불가하다면
# 4. 해당 경로를 추가. (N-1)개 경로까지
# 5. 낮은 비용 순으로 추가 되었으므로 가장 마지막에 추가된 경로를 제거하면
# 6. 두 마을 경로의 유지비 합이 최소

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

N, M = map(int, sys.stdin.readline().split())
pq = PriorityQueue()
parent = [i for i in range(N+1)]

# 가중치 순으로 우선순위 큐에 집어 넣음
for _ in range(M):
    fr, to, cost = map(int, sys.stdin.readline().split())
    pq.put((cost, fr, to))

cnt = 0     # 경로의 수
total = 0   # 가중치의 합
# 연결된 경로의 수가 V-1일 때까지
while cnt < N - 1:
    # 하나씩 꺼내서
    cost, fr, to = pq.get()
    if find(fr) != find(to):    # 조상이 같지 않으면(연결이 안 된 점이면)
        union(fr, to)           # 연결
        total += cost           # 해당 비용 추가
        cnt += 1                # 횟수 추가
        
total -= cost                   # 비용이 가장 비싼(마지막에 추가된) 간선 제거

print(total)                    # 가중치 합 출력