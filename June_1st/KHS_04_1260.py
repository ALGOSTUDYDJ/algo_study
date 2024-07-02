
# dfs 함수
def dfs(start):
    stack = [start]
    while stack:
        # 빼고
        node_number = stack.pop()
        # 방문처리
        v_arr[node_number] = 1
        # 출력하고
        print(node_number, end=" ")
        # 방문처리 안된 얘들 stack에 넣기
        for i in i_arr[node_number]:
            if v_arr[i] == 0:
                dfs(i)

# bfs 함수
def bfs(start):
    que = [start]
    while que:
        node_number = que.pop(0)
        if not v_arr[node_number]:
            print(node_number, end=" ")
        v_arr[node_number] = 1
        for i in i_arr[node_number]:
            if v_arr[i] == 0:
                que.append(i)


# 정점 수, 간선 수, 시작 정점 번호
n, m, v = map(int, input().split())

# 인접 리스트 만들기
i_arr = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    i_arr[v1].append(v2)
    i_arr[v2].append(v1)

# 방문 리스트 만들기
v_arr = [0] * (n + 1)

# 얘를 써야하나
for arr in i_arr:
    arr.sort()

# 출력
dfs(v)
# 방문기록 초기화
v_arr = [0] * (n + 1)
print()
bfs(v)
