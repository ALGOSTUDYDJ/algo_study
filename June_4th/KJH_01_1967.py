# 백준 1967. 트리의 지름
import sys
sys.setrecursionlimit(1000000)


# 재귀 함수로 풀이
def recur(node):
    global max_diameter
    # 자식 노드가 없는 경우 0 반환
    if not tree[node]:
        return 0

    # 부모 노드인 경우, 자식 노드들의 가중치를 재귀 함수로 반환받아옴
    # 자식을 아래로 쭉 연결했을때 비용을 정리
    children = []

    for child in tree[node]:
        children.append(child[1] + recur(child[0]))

    # 부모 노드면, 자식 노드들이 연견될 간선의 지름 중 가장 큰걸 최대값으로 검사
    # 검사 후 연결된 단일의 자식 노드의 간선 중 가장 큰 값을 재귀로 반환
    if len(children) >= 2:
        children.sort(reverse=True)
        temp_max = children[0] + children[1]
    else:
        temp_max = children[0]

    max_diameter = max(max_diameter, temp_max)

    return children[0]

# n = 노드 갯수
n = int(input())

tree = [[] for _ in range(n+1)]
max_diameter = 0

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))

recur(1)

print(max_diameter)