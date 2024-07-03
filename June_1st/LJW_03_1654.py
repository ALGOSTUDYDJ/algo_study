# 이분 탐색 다시 감 잡았습니다

N, K = map(int, input().split())
arr = [int(input()) for _ in range(K)]

# 이분 탐색 
start = 1
end = max(arr)

result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(i // mid for i in arr)
    
    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)