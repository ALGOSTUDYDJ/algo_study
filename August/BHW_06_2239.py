# 2239. 스도쿠

# 1. 빈칸(0)을 순회하며 1~9까지의 값을 차례로 삽입한다.
# 2. 삽입 후, 행, 열, 3x3 사각형 검사를 하며 중복 값이 있는지를 조사한다.
# 3. 중복 값이 있다면, 해당 위치의 해당 수는 틀린 케이스이므로 다음 수를 집어넣는다.
# 4. 이를 빈 칸을 모두 채울 때까지 수행한다.(깊이가 빈 칸의 수가 될 때까지)

# 행 검사
def checkRow(r, c, num):
    # 해당 행에서 같은 수가 있다면 False, 아니면 True
    for x in range(9):
        # 자신의 위치는 확인하지 않음
        if c != x and num == sudoku[r][x]:
            return False
    return True

# 열 검사
def checkCol(r, c, num):
    # 해당 열에서 같은 수가 있다면 False, 없다면 True
    for x in range(9):
        if r != x and num == sudoku[x][c]:
            return False
    return True


# 3x3 사각형 검사
def checkSquare(r, c, num):
    # 3x3 사각형의 좌상단 점 탐색 
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    # 좌상단 점에서 같은 수가 있다면 False, 없다면 True
    for x in range(3):
        for y in range(3):
            if r != nr + x and c != nc + y and sudoku[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth, r, c, num):  # 깊이, 행, 열, 해당 위치의 숫자
    if depth > 0:
        # 행 검사 실패 시 틀림
        if not checkRow(r, c, num):
            return
        # 열 검사 실패 시 틀림
        if not checkCol(r, c, num):
            return
        # 3x3 사각형 검사 실패 시 틀림
        if not checkSquare(r, c, num):
            return
    # 0의 개수에 도달했다면(모든 빈 칸을 채운 경우)
    if depth >= len(zeros): 
        # 결과 출력
        for k in range(9):
            print(''.join(map(str, sudoku[k])))
        exit()  # 프로그램 종료
    
    nr, nc = zeros[depth]    # 0의 좌표를 dfs를 돈다.
    for j in range(1, 9 + 1): # 1부터 9까지
        sudoku[nr][nc] = j    # 해당 수를 입력하고
        dfs(depth + 1, nr, nc, j) # 탐색 진행
        sudoku[nr][nc] = 0    # 원위치


sudoku = []
zeros = [] # 2차원 9*9 리스트를 1차원적으로 생각하여 dfs를 돌기 때문에 좌표들을 튜플형식으로 넣는다.
for i in range(9):
    temp = list(map(int, input()))  # 줄을 입력 받음
    for j in range(9):              # 비어 있는 지점의 좌표를 삽입    
        if temp[j] == 0:
            zeros.append((i, j))
    sudoku.append(temp)             # 스도쿠 배열에 추가

dfs(0, 0, 0, 0)