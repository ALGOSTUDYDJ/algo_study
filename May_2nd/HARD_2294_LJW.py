n, k = map(int, input().split())  # 동전 개수 n과 목표  k
coins = list(int(input()) for _ in range(n))  # 각 동전의 가치를 리스트로 저장
dp = [10001] * (k + 1)  # 동전 개수 저장 DP 테이블 


dp[0] = 0  

for coin in coins:  # 모든 동전
    for i in range(coin, k + 1):  #  목표까지 순회
        dp[i] = min(dp[i], dp[i - coin] + 1)  # 최소 동전 개수 갱신

if dp[-1] == 10001:  #만들 수 없는 경우
    print(-1)
else:  #만들 수 있는 경우
    print(dp[-1])  #동전 개수 출력