N = int(input())  
table = [list(map(int, input().split())) for _ in range(N)]  # 기간, 금액


# DP 초기화
# dp[i] : i번째 날부터 시작하여 얻을 수 있는 최대 보상 저장함
# 크기를 N+1로 잡아야 N일째에서 다음날 참조할 때 인덱스 에러가 안남
dp = [0] * (N + 1)

# 마지막 작업부터 첫 번째 작업까지 역순으로 확인
# Bottom-up 
for i in range(N - 1, -1, -1):
    time, price = table[i]
    if i + time <= N:
        # N일 안쪽으로 끝날 수 있으면 
        # 금액이 더 큰쪽으로 선택
        # 현재 작업 수행 o 최대보상 더하기 vs 현재 작업 x 다음날로 넘어감
        dp[i] = max(price + dp[i + time], dp[i + 1])

    else:
        # N일 밖으로 나가는 일은 수행 못하고 그 전까지 누적한 금액 가져옴
        dp[i] = dp[i + 1]


print(dp[0])