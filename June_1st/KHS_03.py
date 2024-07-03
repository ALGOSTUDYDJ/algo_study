
def bfs():
    
    que = []
    
    # start
    que.append((0, 0, 1))
    arr[0][0] = 3
    
    while que:
        
        x, y, z = que.pop(0)
        
        # 종료 조건
        if x == n - 1 and y == m - 1:
            print(z)
            break 
        
        # que 채우기
        for d in dir:
            ni = x + d[0]
            nj = y + d[1]
            
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                que.append((ni, nj, z + 1))
                # 방문처리
                arr[ni][nj] = 3


# 미로 만들기
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
bfs()
