# 15681. 트리와 쿼리

# 1. 트리의 정보를 입력 받는다.
# 2. 루트 노드의 정점 수를 셈
# 3. 루트 노드의 정점 수는 루트 노드의 자식 노드를 루트로 하는 서브트리의 정점 수 합과 같음
# 4. 최종적으로 배열에는 해당 정점을 루트 노드로 하는 서브 트리의 정점 수가 저장
# 5. 입력에 따른 결과 출력

import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

# 정점의 수, 루트의 번호, 쿼리의 수
N, R, Q = map(int, input().split()) 
# 트리 생성
tree = [[] for _ in range(N+1)]
# 해당 정점을 루트 노드로 하는 서브트리의 정점 수 저장 배열
DP = [-1 for _ in range(N+1)]   

# 간선 정보 입력
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 정점의 수를 찾는 함수
def find(node):
    DP[node] = 1                # 루트 노드는 서브트리의 첫 정점
    for next in tree[node] :    # 연결된 정점들을 순회하며
        if DP[next] == -1 :     # 미방문 정점인 경우(루트 노드로부터 더 깊은 경우)
            DP[node] += find(next)  # 해당 정점을 루트로 하는 서브트리의 정점 수를 더함
    
    return DP[node]             # 해당 서브트리의 정점 수 반환

find(R) # 루트를 시작으로 탐색 진행

# 쿼리 입력
for _ in range(Q) :
    U = int(input())
    sys.stdout.write(f'{DP[U]}\n')