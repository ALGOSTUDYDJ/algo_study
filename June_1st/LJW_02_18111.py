#  가능한 높이 설정후 모두 평탄화 시도
N, M, B = map(int, input().split())
arr = []
for _ in range(N):
    arr += list(map(int, input().split()))

# 높이 설정
min_height = min(arr)
max_height = max(arr)

min_time = float('inf')
height = 0

# 모든 높이 시도
for i in range(min_height, max_height + 1):
    add_blocks = 0
    remove_blocks = 0
    
    for j in arr:
        if j < i:
            add_blocks += (i - j)
        elif j > i:
            remove_blocks += (j - i)
    
    if remove_blocks + B >= add_blocks:
        time_needed = remove_blocks * 2 + add_blocks
        if time_needed <= min_time:
            min_time = time_needed
            height = i

# 결과 출력
print(min_time, height)
