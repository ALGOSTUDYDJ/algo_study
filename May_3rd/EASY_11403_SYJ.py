# - dfs로 풀었습니다.

n = int(input())  
graph = [list(map(int, input().split())) for _ in range(n)]  
visited = [0 for _ in range(n)]  

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:  
            visited[i] = 1 
            dfs(i)  

visited = [0 for _ in range(n)]  
for i in range(n):  # 모든 노드에 대해 반복
    dfs(i)  # 해당 노드에서 DFS를 시작
    for j in range(n):  # 모든 노드에 대해 반복하며
        if visited[j] == 1:  # 해당 노드를 방문했다면
            print(1, end=' ')  # 1을 출력
        else:
            print(0, end=' ')  # 해당 노드를 방문하지 않았다면 0을 출력
    print()  
    visited = [0 for _ in range(n)]  