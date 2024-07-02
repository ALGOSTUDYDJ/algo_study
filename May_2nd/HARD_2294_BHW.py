# 2294. 동전 2


# 적용 알고리즘 : DP
# 1. k원까지의 동전의 개수를 저장할 배열을 작성한다. 기본값은 1
# 2. 동전의 종류를 순회한다. 해당 동전 가치에 필요한 동전의 수는 1
# 3. 1원부터 (k-해당 동전가치)원까지 순회한다.
# 4. 만약 현재 순회중인 동전까지 필요한 동전의 수가 -1개 즉, 방법이 없다면 무시한다.
# 5. 현재 순회 중인 가치 + 동전 가치 까지 경우의 수가 없었다면 현재 순회 중인 가치까지의 동전 수 + 1을
# 6. 있었다면 최솟값을 갱신한다.
# 7. K원을 만드는 최소 가짓수를 출력

import sys

n, k = map(int, sys.stdin.readline().split())   # 동전의 종류, 가치
values = [int(sys.stdin.readline()) for _ in range(n)]
# 정렬 후 중복 동전 및 사용되지 않을 동전들 제외
values.sort()
for i in range(n):
    if values[i] > k:
        values = values[:i]
        break
values = list(set(values))
# DP
DP = [-1]*(k+1)

# 동전의 가치를 순회
for coin in values:
    # 해당 동전까지의 경우의 수는 1
    DP[coin] = 1
    # 1원부터 목표 가치 - 해당 동전 가치까지 순회
    for now in range(1, k-coin+1):
        # 현재 가치를 만들 수 있으면 
        if DP[now] != -1:
            # 기존에 존재한 가짓수가 있었으면
            if DP[now+coin] != -1:
                # 최솟값 갱신
                DP[now+coin] = min(DP[now]+1, DP[now+coin])
            # 없었으면
            else:
                # 현재 가치를 만드는 최소 가짓수 + 1
                DP[now+coin] = DP[now]+1

print(DP[-1])