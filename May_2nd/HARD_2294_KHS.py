
# 입력을 받습니다.
n, k = map(int, input().split())

# 동전의 값을 리스트에 append 해줍니다.
arr = []
for _ in range(n):
    arr.append(int(input()))
    
# dp 테이블 생성 및 초기화
INF = k + 1
dp = [INF] * (k + 1)
dp[0] = 0

# 동전을 목표하는 값까지 순회합니다.
for coin in arr:
    for j in range(1, k + 1):
        if j - coin >= 0:
            # 해당 부분에서 최소 동전의 개수를 갱신해줍니다.
            dp[j] = min(dp[j], dp[j - coin] + 1)

ans = dp[k]
# 값이 초기값이면 만들 수 없는 경우이기 때문에 -1로 갱신
if ans == INF:
    ans = -1
# 그리고 결과를 출력합니다.
print(ans)
