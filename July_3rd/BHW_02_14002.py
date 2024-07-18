# 14002. 가장 긴 증가하는 부분 수열 4

# 1. 첫 번째 원소부터 순회하며 해당 원소의 다음 원소부터 마지막 원소까지
# 2. 첫 번째 원소보다 큰 원소에 대해 가장 긴 부분 수열인지 확인 후 갱신
# 3. 1, 2번을 N번째 원소까지 반복
# 4. 가장 긴 부분 수열과 길이를 출력

N = int(input())
nums = list(map(int, input().split()))

DP = [[i] for i in nums]    # i번째 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열
max_length = 1  # 가장 긴 증가하는 부분 수열의 길이
max_idx = 0     # 부분 수열의 마지막 원소의 인덱스

# N개의 원소를 순회하며
for i in range(N):
    for j in range(i+1, N):
        # j번째 원소가 i번째 원소보다 크다면
        if nums[i] < nums[j]:
            # j번째 원소까지의 수열의 길이가 i번째 수열의 길이 이하인 경우
            if len(DP[i]) >= len(DP[j]):
                DP[j] = DP[i] + [nums[j]]   # 부분 수열 갱신
                if len(DP[j]) > max_length: # 최장 길이인 경우
                    max_idx = j             # 최장 인덱스와 길이 갱신
                    max_length = len(DP[j])

print(max_length)   # 길이
print(*DP[max_idx]) # 부분 수열