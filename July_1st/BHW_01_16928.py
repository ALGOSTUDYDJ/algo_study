# 16928. 뱀과 사다리 게임

# 1. 사다리와 뱀의 정보를 이용해 해당 칸에 도달할 경우 어느 칸으로 이동하는지를 저장
# 2. 너비 우선 탐색으로 100 지점까지 이동한다.
# 3. 100번 칸에 도달한 경우 이동횟수를 반환한다.

N, M = map(int, input().split()) # 사다리의 수, 뱀의 수

board = [i for i in range(101)]     # 게임 판
visited = [0]*101                   # 방문 배열
for _ in range(N+M):
    s, e = map(int, input().split())
    board[s] = e        # 도착지로 이동

# 너비 우선 탐색 함수
def bfs():
    # 1번 칸이 바로 100번 칸과 연결된 경우 주사위를 굴릴 필요 없음
    if board[1] == 100:
        return 0
    q = [1]         # 큐 역할을 할 배열
    visited[1] = 1  # 1번 칸은 방문
    cnt = 1         # 던지는 횟수 초기화
    while True:
        new_q = []
        for t in q:
            for i in range(6, 0, -1):
                # 100번 칸을 넘어간 경우 이동 불가
                if t + i > 100:
                    continue
                # 방문한 경우 탐색 필요 X
                if visited[t + i]:
                    continue
                # 이동 지점이 100이면 종료
                if board[t + i] == 100:
                    return cnt
                # 아닌 경우 다음 탐색지로 추가 및 방문 표시
                new_q.append(board[t + i])
                # 두 지점 모두 처리해 주어야 하는 것에 주의
                visited[t + i] = 1
                visited[board[t + i]] = 1
        
        cnt += 1    # 던지는 횟수 증가
        q = new_q

result = bfs()  # 너비 우선 탐색 진행
print(result)