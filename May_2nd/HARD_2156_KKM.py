n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))


def find_max(arr):
    if len(arr) == 1: # 와인 1개일 때
        return arr[0] 
    if len(arr) == 2: # 와인 2개일 때
        return arr[0] + arr[1]
    # 와인이 3개 이상일 때
    dp = [0]*n

    # 3개 일 때 (dp[2])는 다음과 같이 구한다. 
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    # dp[2] : 다음 세 가지 경우 중에 최대를 답으로 하면 됨
        # 1. 현재를 선택 안함X = 그 직전까지를 그대로 가져오면 됨 = dp[1]
        # 2. 현재를 선택함O = 앞의 상황을 따져야함 => X O  또는 O O 두가지
        # 중에 최대
    dp[2] = max(dp[1], wine[2] + wine[1], wine[2] + wine[0]) 

    for i in range(3,n):
        # 잔 네개일떄도 위와 같은 방식으로 풀면 됨
        # 1. 현재X = 직전 그대로 가져옴 = dp[i-1]
        # 2. 현재 O = X O 인 경우 = 앞앞꺼 dp[i-2] 가져오고 지금꺼 wine[i] 더함
        # 3. 현재 O =  O O 인 경우 = X O O 임 = 앞앞앞꺼 dp[i-3] 가져오고 wine[i] wine[i-1] 더함
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1] )
    return dp[len(arr)-1]
print(find_max(wine))