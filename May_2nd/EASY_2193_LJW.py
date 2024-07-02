# 피보나치 수열을 메모이제이션 이용해서 구현
n = int(input())
if n == 1:
    print(1)
else:
    dp = [0] * n
    dp[0] = 1 
    dp[1] = 1
    for i in range(2, n):
        # dp[n]=dp[n-2]+dp[n-1]
        dp[i] = dp[i - 2] + dp[i - 1] 
    print(dp[n - 1])