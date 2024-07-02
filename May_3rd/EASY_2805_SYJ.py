N, M = map(int, input() .split())
tree = list (map(int, input().split()))
start, end = 1, max(tree) # 최솟값은 1 최댓값은 max(tree)
while start <= end:
    mid = (start + end) // 2
    tree_length = 0
#나무 자르기
    for i in tree:
        if mid <= i:
            tree_length += i - mid
    if tree_length >=  M: # 현재 자른 나무들의 합이 M보다 크거나 같으면
        start = mid + 1  # 절단기 높이를 올린다
    else: # 그렇지 않다면 
        end = mid - 1 # 절단기 높이를 내린다
print(end)