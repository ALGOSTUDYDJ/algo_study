N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  



# bfs 함수
    # 각 정점에서 다른 정점까지 경로를 확인하기
    # 인접 행렬을 받았을 때 정점사이의 연결 여부를 알 수 있음
def bfs(s):
    visited = [0] * N
    lst = []
    lst.append(s)
    
    while lst:
        v = lst.pop()
        for k in range(N):
            if arr[v][k] == 1 and visited[k] == 0:
                visited[k] = 1
                lst.append(k)
    return visited

# 각 정점에서 BFS 수행하여 경로 여부 확인
result = []
for i in range(N):
    result.append(bfs(i))

# print(result) [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# 결과
for row in result:
    print(*row)