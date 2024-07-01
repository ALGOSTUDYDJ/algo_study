# 백준 1149. RGB 거리
import sys

# DP 문제
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# i번 집까지 칠하는 최소 비용은 i-1번째 집에 i번째와 같은 색을 칠하지 않을 때의 비용 중 최소값 + i번째 집 비용

N = int(input())

# 입력받을 금액 초기화
costs = [[] for _ in range(N)]
# dp 배열 초기화
dp = [[1000000 for _ in range(3)] for _ in range(N)]

# N 번 순회하며 입력
for i in range(N):
    costs[i] = list(map(int, sys.stdin.readline().split()))

# N 번 순회하며
for i in range(N):
    # 0, 1, 2 색을 순회하면서 DP 완성시켜나감
    for j in range(3):
        if not i:
            dp[i][j] = costs[i][j]
        else:
            dp[i][j] = min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3]) + costs[i][j]

print(min(dp[N-1]))