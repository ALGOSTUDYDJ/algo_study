# 1456. 거의 소수


# 1. 거의 소수 : 소수의 N제곱 수
# 2. 10의 7승까지의 소수 여부를 구한다.(그 이후는 제곱해서 10의 14승이 되지 않는다)
# 3. 2부터 10의 7승까지 소수를 제곱하며 A, B 범위 내의 거의 소수의 수를 구한다.

import math

A, B = map(int, input().split())
nums = [i for i in range(10000001)]  # 10의 7승까지

# 이 수가 소수인지 확인(에라토스테네스의 체를 이용)
for i in range(2, int(math.sqrt(len(nums)))+1):
    if nums[i] == 0:
        continue
    # 배수도 소수가 아니므로 처리
    for j in range(2*i, len(nums), i):
        nums[j] = 0

cnt = 0     # 거의 소수의 수

# 10의 7승까지 거의 소수의 수를 구한다
for i in range(2, 10000001):
    # 값이 0인 것은 소수가 아니므로 확인하지 않음
    if nums[i] != 0:
        tmp = nums[i]               # 확인할 소수
        while nums[i] <= B / tmp:   # nums[i]를 곱해서 B를 넘지 않을 때까지
            if nums[i] >= A / tmp:  # 소수의 제곱수가 A를 넘은 경우에만 거의 소수로 처리
                cnt += 1
            tmp = tmp*nums[i]       # +1제곱 진행

print(cnt)      # 수 출력