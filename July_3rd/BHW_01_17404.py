# 17404. RGB 거리 2

# 1. 첫 번째 집의 색을 고정한다.
# 2. 두 번째 집부터 N번째 집까지의 누적 최솟값을 갱신한다.
# 3. 마지막 집의 색이 첫 번째 집과의 색과 다른 경우와 이전 최솟값을 비교한다.
# 4. 위 과정을 첫 번째 집의 색을 바꿔가며 반복한 후, 최종 최솟값을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())    # 집의 수

# 각 줄의 집을 칠하는 데 드는 비용
homes = [list(map(int, input().split())) for _ in range(N)]

result = 1000001    # 최솟값

for i in range(3):
    DP = [[1001 for _ in range(3)] for _ in range(N)]
    DP[0][i] = homes[0][i]  # 첫 번째 집의 색 고정
    # 각 j번째 집의 색깔을 정한다.
    for j in range(1, N):
        DP[j][0] = min(DP[j - 1][1], DP[j - 1][2]) + homes[j][0]    # j번째 집의 색이 빨간색
        DP[j][1] = min(DP[j - 1][0], DP[j - 1][2]) + homes[j][1]    # j번째 집의 색이 초록색
        DP[j][2] = min(DP[j - 1][0], DP[j - 1][1]) + homes[j][2]    # j번째 집의 색이 파란색
    
    # 첫 번째 집의 색과 마지막 집의 색이 다른 두 경우에 대해 최솟값 계산
    result = min(result, DP[-1][(i + 1)%3], DP[-1][(i + 2)%3])

print(result)