# 17471 게리맨더링
# 1. 먼저 구역을 나눠줍니다.(좌측, 우측)
# 2. 각 구역이 연결되었는지 확인해줍니다.
# 3. 연결되었다면 해당 구역의 인구 합을 연결되지 않은 경우 0을 반환합니다.
# 4. 두 구역이 모두 연결된 경우 구역간 인구 수 차의 최소를 갱신해줍니다.

from collections import deque

# 연결 여부 확인
def is_con(graph):
    q = deque()
    used = [0]*N
    q.append(graph[0])
    used[graph[0]] = 1
    cnt = 1     # 확인한 원소의 수
    total = 0   # 인구 합
    # bfs 방법으로 연결 여부와 인구 합을 탐색합니다.
    while q:
        t = q.popleft()
        total += populs[t]
        for i in adjl[t]:
            if i in graph and not used[i]:
                used[i] = 1
                cnt += 1
                q.append(i)
    # 모든 구역이 연결되어 있다면 인구 합을 반환하고
    if cnt == len(graph):
        return total
    # 그렇지 않은 경우 0을 반환합니다.
    else:
        return 0

# 구획 나누는 함수
def dividing(i, pre, limit):
    global min_diff
    # 구역 limit에 도달시
    if i == limit:
        # 좌측, 우측 구역 정의
        left, right = [], []
        for j in range(N):
            # 좌측 구역에 추가
            if visited[j]:
                left.append(j)
            # 우측 구역에 추가
            else:
                right.append(j)
        # 좌측 구역의 인구수
        resl = is_con(left)
        if resl:
            # 우측 구역의 인구수
            resr = is_con(right)
            if resr:
                # 지역구 간 최소 인구수 갱신
                min_diff = min(min_diff, abs(resl-resr))
                return
            return
        return
    
    # limit에 도달하지 못한 경우
    for j in range(pre+1, N-limit+i+1):
        if visited[j]:
            continue
        visited[j] = 1
        dividing(i+1, j, limit)
        visited[j] = 0


left = []
right = []
N = int(input())                            # 구역의 수
populs = list(map(int, input().split()))    # 각 구역별 인구
adjl = [[] for _ in range(N)]

for i in range(N):
    inputs = list(map(int, input().split()))
    for j in inputs[1:]:
        adjl[i].append(j-1)
    

min_diff = 1e9

# 왼쪽 지역구의 구역 수를 n개로 하여 분할 후 계산
for n in range(1, N//2+1):
    visited = [0]*N
    dividing(0, -1, n)

if min_diff==1e9:
    print(-1)
else:
    print(min_diff)