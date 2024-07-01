# 입력 처리
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 초기화 (index: 0- top, 1-북, 2-동, 3-서, 4-남, 5-bottom)
dice = [0, 0, 0, 0, 0, 0]

# 방향 벡터
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

'''
dice[0]: top
dice[1]: 북 north
dice[2]: 동 east
dice[3]: 서 west
dice[4]: 남 south
dice[5]: bottom

'''

# 주사위 굴리기 함수
def mydice(direction):
    top, north, east, west, south, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:  # 동쪽으로
        dice[0], dice[2], dice[5], dice[3] = west, top, east, bottom
    elif direction == 2:  # 서쪽
        dice[0], dice[3], dice[5], dice[2] = east, top, west, bottom
    elif direction == 3:  # 북쪽
        dice[0], dice[1], dice[5], dice[4] = south, top, north, bottom
    elif direction == 4:  # 남쪽
        dice[0], dice[4], dice[5], dice[1] = north, top, south, bottom

# 명령 수행
for command in commands:
    nx, ny = x + dx[command - 1], y + dy[command - 1]

    # 지도 밖으로 나가는 경우
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    # 위치 갱신
    x, y = nx, ny

    # 주사위 굴리기
    mydice(command)

    # 지도와 주사위 상호작용
    if board[x][y] == 0:
        board[x][y] = dice[5]  # 주사위 바닥면 값 복사
    else:
        dice[5] = board[x][y]  # 칸의 값이 주사위 바닥면으로 복사
        board[x][y] = 0

    # 주사위 윗면 값 출력
    print(dice[0])

