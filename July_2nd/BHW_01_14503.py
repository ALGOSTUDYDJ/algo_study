# 14503. 로봇 청소기

# 알고리즘대로 구현(숫자를 따라갈 것)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 북, 동, 남, 서
N, M = map(int, input().split())            # 세로, 가로
r, c, d = map(int, input().split())         # 현재 좌표
board = [list(map(int, input().split())) for _ in range(N)]

total = 0   # 청소한 칸의 수
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소한다.
    if board[r][c] == 0:
        total += 1          # 청소한 칸의 수 증가
        board[r][c] = -1    # 청소했음을 표시
    
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    uncleaned = False
    for i in range(1, 5):
        now = dirs[(d - i) % 4]     # 반시계 방향 회전
        dr = r + now[0]
        dc = c + now[1]
        # 3. 빈 칸이 있는 경우
        # 3.1. 반시계 방향 90도 회전
        if 0 <= dr < N and 0 <= dc < M and board[dr][dc] == 0:
            uncleaned = True
            # 3.2. 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            r, c = dr, dc
            d = (d - i) % 4
            break
    # 3.3. 1번으로 돌아감
    if uncleaned:
        pass
    else:
        back = dirs[(d + 2) % 4]
        dr = r + back[0]
        dc = c + back[1]
        # 2.1. 후진 가능하면 후진(방향이 바뀌지 않는 것에 주의)
        if 0 <= dr < N and 0 <= dc < M and board[dr][dc] != 1:
            r, c = dr, dc
        # 2.2. 후진 불가능하면 작동 중지
        else:
            break

print(total)