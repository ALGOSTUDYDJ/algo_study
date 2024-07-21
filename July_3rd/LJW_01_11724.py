import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(v): # dfs로 시작
    visited[v] = True  
    for i in graph[v]:  
        if not visited[i]:  
            dfs(i)  # 재귀

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
# 순회
for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않은 정점
        dfs(i)  # DFS
        cnt += 1  

print(cnt)
