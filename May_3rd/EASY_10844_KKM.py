
N = int(input().strip())

# 길이가 N인 계단 수를 저장할 DP
dp = [[0] * 10 for _ in range(N + 1)]

# dp[i][j] 길이가 i, 마지막 자릿수가 j인 계단 수의 개수
for j in range(1, 10):


    # dp[1][1]부터 dp[1][9]까지는 1임
    dp[1][j] = 1



# 길이가 2 이상인 경우
for i in range(2, N + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]  # j-1로 끝나는 계단수에 j를 추가
        if j < 9:
            dp[i][j] += dp[i-1][j+1]  # j+1로 끝나는 계단수에 j를 추가
        dp[i][j] %= 1000000000  # 나눈 다음에 저장하기


result = 0
for j in range(10):
    result += dp[N][j]
    result %= 1000000000


print(result)
