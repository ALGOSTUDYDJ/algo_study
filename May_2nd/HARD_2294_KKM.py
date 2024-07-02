n, k = map(int, input().split())


coins = []
for _ in range(n):
    coins.append(int(input()))


# 인덱스 = 0...x... k 까지 = x 원 만들기 위한 최소 개수
# 최대한 큰 값인 무한대로 저장
dp = [float('inf')] * (k + 1)

# 0원을 만들기 : 최소 동전 개수는 0개임
dp[0] = 0

# 동전 리스트의 각각의 동전을 기준으로 한다.
for coin in coins:
    # coin 원을 이용해서 만들 수 있는 것은 최소 coin원부터 시작해야함
    # coin(원) 부터 k원까지 
    for i in range(coin, k + 1):
        # 현재 금액(i)을 만들기 위한 최소 동전 개수
        # 지금 현재 coin 이고, i원을 만들기 위해서는
        # coin 1개와 (i - coin)원 만드는 것을 합친다 즉 dp[i - coin] + 1
        # 둘을 비교해서 최소를 선택함
        dp[i] = min(dp[i], dp[i - coin] + 1)

# k원을 만들 수 없는 경우 : -1
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
