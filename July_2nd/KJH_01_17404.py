# 백준 17404. RGB거리 2
import sys

# RGB 거리 문제와 거의 유사한 문제이지만, 조건 1개 초가
# 추가된 조건 : 1번 집과 N번 집이 같은 색상이면 안됨
# 기존처럼 시작 색상의 정보 없이 DP로 풀이하면 마지막 인덱스(N-1)에서 초기값에 대한 정보가 없음
# 시작 색상에 따라 마지막에 추출해야할 최소값 정보가 달라지므로, 3 개의 리스트로 분리해서 DP를 진행함

N = int(sys.stdin.readline())

houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start_with = [[[float('inf')] * 3 for _ in range(N)] for _ in range(3)]

# 2번 집 비용 하드코딩 -> 처음과 두 번째 동일하게 칠하는 경우는 없어야하므로 float('inf') 값으로 유지되도록 둔다.
start_with[0][1][1] = houses[0][0] + houses[1][1]
start_with[0][1][2] = houses[0][0] + houses[1][2]

start_with[1][1][0] = houses[0][1] + houses[1][0]
start_with[1][1][2] = houses[0][1] + houses[1][2]

start_with[2][1][0] = houses[0][2] + houses[1][0]
start_with[2][1][1] = houses[0][2] + houses[1][1]

# 2부터 N-1까지 순회. 각 시작 색상을 기준으로 시작해서, N-1 열까지 칠하는 데에 가장 비용이 적게 드는 경우를 전부 구함.
for i in range(2, N):
    for j in range(3):
        start_with[j][i][0] = min(start_with[j][i-1][1], start_with[j][i-1][2]) + houses[i][0]
        start_with[j][i][1] = min(start_with[j][i-1][0], start_with[j][i-1][2]) + houses[i][1]
        start_with[j][i][2] = min(start_with[j][i-1][0], start_with[j][i-1][1]) + houses[i][2]

# 최속밧을 저장할 리스트 0으로 초기화
mins = [0] * 3

# 이중 반복문을 통해서, 각 시작 색상별 최소값을 구함.
# 이 때, N-1번 인덱스 리스트에서 시작 색상과 같은 경우는 제외
for i in range(3):
    temp_min = float('inf')
    
    for j in range(3):
        if i != j:
            temp_min = min(temp_min, start_with[i][N-1][j])
    
    mins[i] = temp_min

print(min(mins))