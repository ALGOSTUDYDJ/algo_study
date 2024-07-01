# 15686. 치킨 배달
from itertools import combinations


# 튜플 A, B 사이의 거리를 반환
def min_dist_chicken(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


N, M = map(int, input().split())

# 0: 빈칸, 1: 집, 2: 치킨집
city = [list(map(int, input().split())) for _ in range(N)]

# 도시를 순회하면서 집, 치킨집의 위치를 밸도 배열에 튜플로 저장
homes = []
chickens = []


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 풀이 순서

min_chicken_dist = float('inf')

# DFS로 풀이
# 치킨집 M 개를 조합
m_chickens = combinations(chickens, M)

# 각 집에 대해 선택한 M개의 치킨집에 대한 거리를 구하고
for chicken in m_chickens:
    dist = 0
    for home in homes:
        # 각 집에서 가장 가까운 치킨집을 구함
        min_dist = float('inf')
        for j in range(M):
            min_dist = min(min_dist, min_dist_chicken(chicken[j], home))

        # 각 집에서의 구해진 치킨 거리를 합해서 저장
        dist += min_dist
    # 모든 집에서의 치킨 거리 계산이 끝난 뒤, 저장된 결과와 비교하여 최소값 저장
    min_chicken_dist = min(dist, min_chicken_dist)

print(min_chicken_dist)