# 1976. 여행 가자


# 1. 각 도시의 연결 여부 행렬을 순회하며 연결된 도시의 대표 도시를 선정
# 2. 여행 경로대로 순회하면서 시작 도시와 연결이 되어 있지 않다면(대표 도시가 다른 경우) 여행 불가
# 3. 모든 경로의 도시가 시작 도시와 연결되어 있을 경우(대표 도시가 같은 경우) 여행 가능
import sys

N = int(sys.stdin.readline())       # 도시의 수
M = int(sys.stdin.readline())       # 여행 계획에 속한 도시의 수

# 도시의 연결여부 행렬
adjm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
parent = [i for i in range(N+1)]    # 조상 배열
# 여행 계획
plan = list(map(int, sys.stdin.readline().split()))

# 조상을 찾는 함수
def find(a):
    # 자신이 조상이면 자신 반환
    if a == parent[a]:
        return a
    # 아니라면 조상을 찾는다
    else:
        parent[a] = find(parent[a])
        return parent[a]

# 두 노드의 조상을 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    # 두 노드의 조상이 다르다면 a 쪽으로 합침
    # 같다면 합칠 필요 없음
    if a != b:
        parent[b] = a

# N개의 도시쌍을 순회하면서
for i in range(N):
    for j in range(N):
        # 서로 연결된 도시이면 하나의 대표 도시 선정
        if adjm[i][j]:
            union(i, j)

# 시작 도시의 대표 도시를 찾는다
start = find(plan[0]-1)

# 여행 가능 여부 변수(초기값 True)
isPossible = True
# 최초 1개 도시 제외 M-1개의 도시를 순회하며
for i in range(1, M):
    # 시작 도시의 대표 도시와 현재 도시의 대표 도시가 다르면
    if start != find(plan[i]-1):
        # 여행 불가
        isPossible = False
        break

# 여행 가능 시 YES, 불가 시 NO
if isPossible:
    print('YES')
else:
    print('NO')
