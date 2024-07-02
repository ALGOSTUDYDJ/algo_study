N, M = map(int, input().split())
trees = list(map(int, input().split()))


left = 0  # 최소 
right = max(trees)  # 최대(제일높은나무)
result = 0

# 이진 탐색 
while left <= right:
    mid = (left + right) // 2
    
    # 현재 mid 높이로 잘랐을 때 얻을 수 있는 나무의 총 길이  
    entire = 0
    for tree in trees:
        if tree > mid:
            entire += tree - mid
    
    # 그것을 M 과 비교
    if entire >= M:
        result = mid  # result 갱신함 (조건 만족하므로)
        left = mid + 1  # 더 높은 절단기 있는지 찾아보기
    else:
        right = mid - 1  # 실패. 더 낮은 절단기 높이로 시도

print(result)