# 1033. 칵테일

# 1. N - 1 쌍의 재료 정보를 저장
# 2. DFS를 이용 각 재료의 비율을 계산
# 3. 전체 비율 정수의 최대공약수를 계산
# 4. 나눈 값을 출력

import sys
input = sys.stdin.readline

N = int(input())    # 칵테일에 들어가는 재료 수
graph = [[] for _ in range(N)]  # 각 재료 간의 비율 정보를 저장하는 그래프
visited = [0]*N     # 각 재료에 대한 탐색 여부를 기록하는 리스트
D = [0]*N           # 각 재료의 상대적인 양을 저장하는 리스트
lcm = 1     # 최소 공배수, 초기값은 1로 설정

# 최대 공약수를 구하는 함수
def gcd(a, b):
    # 나머지가 0이면 최대 공약수는 a
    if b == 0:
        return a
    # 그렇지 않으면 재귀적으로 b와 a % b로 구함
    else:
        return gcd(b, a % b)

# DFS 탐색을 통해 각 재료의 비율을 계산하는 함수
def DFS(v):
    visited[v] = 1  # 현재 노드를 방문 처리
    # 현재 노드에 연결된 다른 노드를 탐색
    for now in graph[v]:
        next = now[0]  # 다음으로 탐색할 노드
        # 다음 노드를 방문하지 않은 경우
        if not visited[next]:
            # 비율을 계산하여 다음 노드의 양을 결정
            D[next] = D[v] * now[2] // now[1]
            # 재귀적으로 DFS 호출
            DFS(next)

# N - 1 쌍의 비율 정보를 입력받음
for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    # a에서 b로의 비율 정보를 저장
    graph[a].append((b, p, q))
    # 반대로 b에서 a로의 비율 정보도 저장 (대칭적 비율)
    graph[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 각 비율(전체)의 최소공배수 갱신

D[0] = lcm  # 첫 번째 재료의 양을 최소 공배수로 설정
DFS(0)      # 첫 번째 재료부터 DFS 탐색 시작

# 모든 재료의 상대적인 양에 대한 최대 공약수 구하기
mgcd = D[0]  # 첫 번째 재료의 양을 기준으로 설정
for i in range(1, N):
    mgcd = gcd(mgcd, D[i])

# 각 재료의 양을 최대 공약수로 나눈 값을 출력(재료 양이 정수이므로)
for i in range(N):
    print(int(D[i] // mgcd), end = ' ')
