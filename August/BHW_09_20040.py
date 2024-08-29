# 20040. 사이클 게임

# 1. 유니온 파인드 알고리즘을 이용한다.
# 2. 각 시행에 대해 두 점이 연결되었는지 판별하고 연결되었다면 사이클이 생긴 것이므로 중단한다.
# 3. 연결되지 않은 경우 두 점을 잇는다.
# 4. 사이클이 생긴 경우 즉각 종료하고 종료된 시점을 출력한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # 점의 개수, 차례의 개수(선분)
parent = [x for x in range(N)]      # 부모 배열

def find(x):            # 부모를 찾는 함수
    while x!= parent[x]:# 최상단 부모에 도달할 때까지(자신이 부모일 때까지)
        x = parent[x]   
    return x            # 부모 반환

def union(x, y):        # 부모를 합치는 함수
    parent_x = find(x)  # 각 점의 부모를 찾음
    parent_y = find(y)
    if parent_x < parent_y: # 부모의 번호가 높은 쪽으로 합침
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

result = 0 # 사이클이 만들어진 차례의 번호를 저장
for i in range(1, M+1): # M개 시행에 대해
    d1, d2 = map(int, input().split())  # 두 개의 점을 입력 받음
    if find(d1) == find(d2):            # 두 점의 부모가 같으면   
        result = i                      # 시행을 기록하고 종료
        break
    union(d1, d2)   # 두 점을 연결
    
print(result)