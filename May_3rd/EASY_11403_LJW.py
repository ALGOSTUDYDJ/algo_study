n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


# k는 중간에 거치는 정점
for k in range(n):
    # i는 출발 정점
    for i in range(n):
        # j는 도착 정점
        for j in range(n):
            # 3중 for 문으로 거쳐가는 거 까지 체크
            # graph[i][k]는 i에서 k 경로
            # graph[k][j]는 k에서 j 경로
            # 둘다있으면 이어진 경로이므로 1
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in graph:
    print(*i)