n = int(input())

# n이 1 또는 2일 경우를 대비
dp = [0] * (n + 1)

dp[1] = 1
if n > 1:
    dp[2] = 2


for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)