# 백준 2294. 동전 2


# 입력 n: 동전 종류, k: 목표 금액
n, k = map(int, input().split())

# 동의 가치를 저장
values = [0] * n

# 동전 가치를 입력
for i in range(n):
    values[i] = int(input())

# 최소값을 구하는 문제로 dp 배열에 큰 수를 저장
# dp[i]는 가치 i를 만들 수 있는 최소 동전의 수
dp = [10e9] * (k+1)
# 0은 만들 수 없으므로, 0으로 저장
dp[0] = 0

# DP 배열 전체를 순회하면서, 동전으로 만들 수 있는지 없는지 계속해서 확인해나감
for i in range(1, k+1):
    for value in values:
        # 가치 i를 만들 수 있는 최소한의 동전 갯수는
        # 1. dp[i - 현재 가치]의 값에 1을 더한 수
        # 2. 혹은 이미 다른 최소값으로 만들어둔 동전 갯수, 둘 중 최소값
        # i - value가 0보다 작으면 -인덱싱이 되므로 제외
        if i - value >= 0:
            dp[i] = min(dp[i], dp[i - value] + 1)
        
# 출력
if dp[k] == 10e9:
    print(-1)
else:
    print(dp[k])
