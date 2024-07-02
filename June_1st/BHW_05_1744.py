# 1744. 수 묶기


# 1. 임의의 두 수를 묶어 곱한 합이 최대가 되게 하려면 부호가 같고 절댓값이 큰 순서대로 묶어야 한다.
# 2. 단, 자연수인 경우 1과 n을 곱하면 그 곱인 n이 그 합인 n+1보다 작으므로 묶지 않는다.
# 3. 0인 경우도 마찬가지로 분리해서 판단한다.
# 4. 따라서 1보다 큰 자연수, 1, 0, 음의 정수로 분류하여 판단한다.
# 5. 먼저 1의 수를 모두 더한다. 
# 6. 1보다 큰 자연수와 음수의 경우 두 수로 묶을 수 없을 때까지 묶어서 그 곱을 더한다.(각 분류의 수가 1개 이하일 때까지)
# 7. 1보다 큰 자연수의 경우 원소가 1개 남았다면 그냥 더한다.
# 8. 음수의 경우 원소가 1개 남았다면 0이 있는 경우 0과 곱하면 되므로 더하지 않고, 아닌 경우 더한다.
# 9. 전체 합을 출력한다.

N = int(input())    # 전체 원소의 수
positives = []      # 1보다 큰 자연수
negatives = []      # 음의 정수
ones = 0            # 1
zeros = 0           # 0

for _ in range(N):
    num = int(input())          # 입력으로 들어오는 수
    if num > 1:                 # 각 분류 기준에 맞게 분류해 저장한다.
        positives.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zeros = 1
    else:
        negatives.append(num)

total = ones                    # 합의 최댓값을 저장할 변수(1의 갯수만큼 시작)

positives.sort()                # 1보다 큰 자연수는 오름차순 정렬한다.
negatives.sort(reverse=True)    # 음의 정수는 내림차순 정렬한다.(마지막 원소의 절댓값이 가장 크게 하도록 하기 위함)

while len(positives) > 1:       # 2개 이상의 원소가 남을 때까지
    num1 = positives.pop()
    num2 = positives.pop()
    total += num1*num2          # 큰 두 수를 곱해 더한다.
else:
    if len(positives):          # 남은 원소가 있다면
        total += positives[0]   # 더한다.

while len(negatives) > 1:       # 2개 이상의 원소가 남을 때까지
    num1 = negatives.pop()
    num2 = negatives.pop()
    total += num1*num2          # 절댓값이 큰 두 수를 곱해 더한다.
else:
    if len(negatives):          # 남은 원소가 있다면
        if zeros == 0:          # 입력으로 0이 주어지지 않은 경우만
            total += negatives[0]   # 그 수를 더한다.

print(total)                    # 총합 출력