# 1167. 트리의 지름

# 1. 입력을 트리 형태(그래프)로 저장한다.(위치, 비용)
# 2. 1번 정점으로부터 가장 먼 지점으로까지의 DFS를 수행한다.(한 쪽 끝 지점으로 이동하기 위함)
# 3. 이동한 가장 먼 지점에서 다른 가장 먼 지점으로까지의 DFS를 수행한다.(다른 한 쪽 끝 지점으로 이동하기 위함)
# 4. 해당 거리가 트리의 지름이 된다.

import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

# DFS 함수(재귀)
# 현재의 정점으로부터 가장 먼(합산 비용이 가장 큰) 정점을 찾는 DFS 함수
def dfs(node, distance):
    global max_distance, farthest_node
    
    # 현재 정점을 방문 처리
    visited[node] = 1
    # 만약 현재까지 합산한 비용이 최대 비용보다 크면,
    # 최대 비용을 갱신시키고 함수를 호출한 시작 노드로부터 가장 비용이 큰 노드를 가장 먼 노드로 설정
    if distance > max_distance:
        max_distance = distance # 비용(거리) 갱신
        farthest_node = node    # 가장 먼 노드
    
    # 트리에 연결된 다른 정점 중에서 방문하지 않은 정점을 방문
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, distance + weight)

V = int(input())    # 정점의 수

# 키에러 방지를 위한 defaultdict 자료 구조 사용
tree = defaultdict(list)

# V개의 정점에 연결된 간선 정보를 입력받음
for _ in range(1, V + 1):
    # 부모 노드, 자식 노드 정보
    parent, *data = list(map(int, input().split()))

    for i in range(0, len(data)-2, 2):
        child = data[i]     # 자식 노드
        weight = data[i+1]  # 자식 노드까지의 비용
        # 인접 리스트로 풀이 부모와 자식 모두에게 서로의 정점 및 비용 정보를 입력함
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))

# 첫 번째 DFS(가장 끝 지점으로 이동)
visited = [0] * (V + 1) # 방문 배열
max_distance = 0        # 최대 거리
farthest_node = 1       # 가장 멀리 있는 노드
dfs(1, 0)               # 1번 노드에서 DFS 수행

# 두 번째 DFS(가장 끝 지점에서 다른 끝 지점으로 이동)
visited = [0] * (V + 1) # 방문 배열 초기화
max_distance = 0        # 최대 거리 초기화
dfs(farthest_node, 0)   # 가장 끝 지점에서 거리 측정 

print(max_distance)