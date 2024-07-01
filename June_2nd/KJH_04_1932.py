# 1932. 정수 삼각형
from copy import deepcopy


N = int(input())

# 완전 이진 트리 형식의 문제이지만,
# 특이한 형식으로 입력이 들어와서 입력 그대로 리스트로 받아 저장해주고 해당 값을 사용함
# DP로 풀이하며, 대각선 위치의 0 ~ N-2까지는 본인 아래의
numbers = [0 for _ in range(N)]

first_row = int(input())
if N == 1:
    print(first_row)
else:
    second_row = [int(x) + first_row for x in input().split()]
    numbers[0], numbers[1] = second_row[0], second_row[1]

    for i in range(2, N):

        # 현재 줄의 입력을 받음
        input_line = list(map(int, input().split()))
        pre_line = deepcopy(numbers)

        # i+1 반복을 돌면서,
        for j in range(i+1):
            if j == 0:
                numbers[0] = input_line[0] + pre_line[0]
            else:
                numbers[j] = input_line[j] + max(pre_line[j-1], pre_line[j])

    print(max(numbers))