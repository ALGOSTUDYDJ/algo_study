# 1717. 집합의 표현


# 1. M 개의 명령에 대해 합집합 명령은 합집합을 조상 비교 명령은 조상 비교를 수행한다.
# 2. 합집합 명령 시 한 쪽 조상에게로 합친다.
# 3. 같은 조상 탐색은 조상이 같다면 YES, 다르다면 NO를 출력한다.

import sys
sys.setrecursionlimit(100000)       # 재귀 제한(명령의 수 만큼)

N, M =map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]

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

# M개의 명령에 대해
for i in range(M):
    order, a, b = map(int, sys.stdin.readline().split())    # 명령, 원소 a, b
    if order:
        # 두 원소의 조상을 찾아서
        paA = find(a)
        paB = find(b)
        # 조상이 같으면 YES 아니면 NO
        if paA == paB:
            print('YES')
        else:
            print('NO')
    # 합집합 명령
    else:
        union(a, b)