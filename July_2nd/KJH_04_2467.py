# 백준 2467. 용액

# 입력
N = int(input())
solutions = list(map(int, input().split()))

# 왼쪽, 오른쪽 포인터 변수 선언 및 초기화
left = 0
right = N - 1

# 결과로 저장해 둘 값 0으로 초기화
result_left = 0
result_right = 0

# 주어지는 정수가 최대 10억으로, 최대가 될 수 있는 2e9로 결과 최소값 초기화
result_abs = 2e9

while left < right:

    temp_sum = solutions[left] + solutions[right]

    # 합의 값이 0에 더 가까운 경우에만 결과값을 저장
    if abs(temp_sum) <= result_abs:
        result_abs = abs(temp_sum)
        result_left = solutions[left]
        result_right = solutions[right]

    # 0이면 바로 종료하고 출력
    if temp_sum == 0:
        result_left = solutions[left]
        result_right = solutions[right]
        break
    elif temp_sum > 0:
        right -= 1
    else:
        left += 1

# 결과 출력
print(result_left, result_right)
