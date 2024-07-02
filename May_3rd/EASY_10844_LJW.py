n = int(input())


dp = [[0] * 10 for _ in range(n + 1)]

# 1자리 평평계단
for i in range(1, 10):
    dp[1][i] = 1

# 자리수 탐색
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 결과 계산
cnt = 0
for i in range(10):
    cnt += dp[n][i]

print(cnt % 1000000000)