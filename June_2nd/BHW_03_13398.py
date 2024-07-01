# 13398. 연속 합 2


N = int(input())
nums = list(map(int, input().split()))

# 왼쪽에서 오른쪽(ltor), 오른쪽에서 왼쪽(rtol) 최대 연속합을 구한다
ltor = [0]*N
rtol = [0]*N
ltor[0] = nums[0]
rtol[-1] = nums[-1]
max_total = ltor[0]

# ltor 최대 연속합
for i in range(1, N):
    # 직전 최대연속합이 음수인 경우 자신이 새 연속합
    ltor[i] = max(nums[i], ltor[i-1] + nums[i])
    # 연속합을 구해준다.
    max_total = max(max_total, ltor[i])

# rtol 최대 연속합
for i in range(N-2, -1, -1):
    rtol[i] = max(nums[i], rtol[i+1]+nums[i])

# ltor[i-1] + rtol[i+1] 을 더하면 i번째 값을 제거한 것과 같다.
# 따라서 다음의 코드는 i번째 값을 제외하고 최대 연속합을 구하는 코드이다.
for i in range(1, N-1):
    # 기존의 max_total과 비교해 제거한 것이 크다면 제거한 값으로 갱신
    max_total = max(max_total, ltor[i-1] + rtol[i+1] )

print(max_total)