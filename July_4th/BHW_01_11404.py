# 11404. 플로이드

# 플로이드-워셜 알고리즘
# A노드에서 B노드까지 최단 경로를 구했다고 가정했을 때 
# 최단 경로 위에 K 노드가 존재한다면 그것을 이루는 부분경로도 최단경로
# 1. 리스트를 선언하고 초기화하기(인접 행렬)
# 2. 최단거리 리스트에 그래프 데이터 저장하기
# 3. 점화식으로 리스트 업데이트하기

import sys
input = sys.stdin.readline
N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수

# 각 도시에서 각 도시로 가는 최단 거리 정보를 저장하는 배열
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

# 같은 도시로 가는 최단 거리는 0
for i in range(1, N+1):
    distance[i][i] = 0

# 각 노선의 최소 비용 정보를 저장(중복 제거)
for i in range(M):
    # 시점, 종점, 비용
    s, e, w = map(int, input().split())
    # 단일 노선 최소 비용 갱신
    if distance[s][e] > w:
        distance[s][e] = w

# 플로이드-워셜
for i in range(1, N + 1):           # 경유지
    for j in range(1, N + 1):       # 출발지
        for k in range(1, N + 1):   # 도착지
            # i 노드를 경유지로 하는 경로가 최단 경로인지 확인 후 갱신
            if distance[j][k] > distance[j][i] + distance[i][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

# 각 지점 사이 최단 거리 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 경로가 없는 경우 0
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        # 경로가 있으면 최단거리 출력
        else:
            print(distance[i][j], end=' ')
    print() # 줄 바꿈