# 11657. 타임머신

# 1. 벨만-포드 알고리즘을 이용해 해당 도시까지의 소요 시간을 구한다.
# 2. 음수 사이클이 있는 경우(무한히 오래 전으로 되돌릴 수 있는 경우) -1 출력
# 3. 없는 경우 최단 소요 시간 출력

# 벨만-포드
# 1. 모든 에지와 관련한 정보를 가져온 후 다음 조건에 따라 거리 리스트의 값 업데이트
# 1.1. 출발 노드가 방문한 적이 없는 노드일 때 값을 업데이트하지 않음
# 1.2. 출발 노드의 거리 리스트값 + 에지 가중치 < 종료노드의 거리 리스트 값 인 경우 종료 노드의 거리 리스트 값 업데이트
# 2. 노드 개수 - 1 번만큼 1을 반복
# 3. 음수 사이클 유무를 알기 위해 모든 에지에 관해 다시 한 번 1을 수행. 한 번이라도 업데이트시 음수 사이클 존재

import sys
input = sys.stdin.readline
N, M = map(int, input().split())    # 도시의 개수, 버스 노선의 수
edges = []
distance = [1e9] * (N + 1)          # 거리 리스트

# 노선 데이터 저장(출발, 도착, 가중치)
for i in range(M): 
    s, e, t = map(int, input().split())
    edges.append((s, e, t))     # 출발 도시, 도착 도시, 가중치(시간) 순 저장

distance[1] = 0

for _ in range(N-1):
    for s, e, t in edges:
        # 출발 도시가 기존에 방문한 도시가 아니면서
        # 출발 도시까지의 시간 + 소요 시간 < 기존 도착 도시 소요 시간인 경우 갱신 
        if distance[s] != 1e9 and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

# 음수 사이클 확인
minus = False
# 각 노선에 대해
for s, e, t in edges:
    # 출발 도시가 미방문이면서
    # 출발 도시까지의 시간 + 소요 시간 < 기존 도착 도시 소요 시간이라면 음수 사이클 존재
    if distance[s] != 1e9 and distance[e] > distance[s] + t:
        minus = True

# 음수 사이클이 없다면
if not minus:
    for i in range(2, N + 1):
        # 방문한 도시인 경우 해당 도시까지 소요 시간 출력
        if distance[i] != 1e9:
            print(distance[i])
        # 미방문 도시인 경우 -1(경로가 없는 경우)
        else:
            print(-1)
# 음수 사이클이 있다면(경로 없음)
else:
    print(-1)
