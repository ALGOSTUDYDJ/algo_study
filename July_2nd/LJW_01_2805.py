def binary_search(trees, target): # 이분 탐색 함수
    start = 0
    end = max(trees)  # 가장 높은 나무 끝점

    result = 0 
    while start <= end:
        total = 0 
        mid = (start + end) // 2
        for i in trees:
            if i > mid: 
                total += i - mid 
        if total < target:
            end = mid - 1 
        else: 
            result = mid 
            start = mid + 1 

    return result

# 입력 
n, m = map(int, input().split())
tree = list(map(int, input().split()))


result = binary_search(tree, m)
print(result)
