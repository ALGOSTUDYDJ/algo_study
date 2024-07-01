# 백준 1987. 알파벳


# 대문자 알파벳으로 이루어진 보드를 지남
# 인덱싱을 편하게 해주기 위해서 알파벳을 정수로 변환해 준 뒤 bfs로 풀이

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(cnt, row, col):

    global max_cnt

    if cnt == 26:
        max_cnt = 26
        return

    max_cnt = max(cnt, max_cnt)

    for d in dirs:
        next_row = row + d[0]
        next_col = col + d[1]
        # 해당 방향으로 갔을 때 보드 위에 있는지 여부 + 이미 방문처리된 알파벳인지 확인
        if 0 <= next_row < R and 0 <= next_col < C and not visited[board[next_row][next_col]]:
            # 방문 가능한 알파벳인 경우 다음 경로로 추가
            visited[board[next_row][next_col]] = True
            bfs(cnt + 1, next_row, next_col)
            visited[board[next_row][next_col]] = False

R, C = map(int, input().split())

visited = [False] * 26

board = [[ord(c)-65 for c in input()] for _ in range(R)]
max_cnt = 0

visited[board[0][0]] = True

bfs(1, 0, 0)

print(max_cnt)

