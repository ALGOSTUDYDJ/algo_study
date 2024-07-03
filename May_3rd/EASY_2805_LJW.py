N, M = map(int, input().split())
tree = list(map(int, input().split()))
low = 0 
high = max(tree) #이진 탐색 검색 범위 설정


while low <= high: # 이진 탐색 
    mid = (low+high) // 2
    
    total = 0 # 나무 길이 카운트
    for i in tree:
        if i >= mid:
            total += i - mid
    
    # 목표길이 체크
    if total >= M: 
        low = mid + 1
    else:
        high = mid - 1
print(high)