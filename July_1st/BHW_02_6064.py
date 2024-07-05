# 6064. 카잉 달력(오래 걸리는 코드)

# 1. 첫 번째 해부터 카잉 달력을 증가시켜가며 원하는 해가 있는지 탐색한다. -> 시간 초과
# 2. x-y를 목표로 하는 차이로 규정한 후, 원하는 차이를 찾는다. 
# 3. step은 M, N 중 작은 값으로 한다.
# 4. 최대 반복 횟수는 40,000 회


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split()) 
    year, i, j = 1, 1, 1 # 연도, x, y 부
    
    goal = x - y # 목표로 하는 차이
    
    # 같다면
    if x == y:
        print(x)
        continue
    
    # 최댓값이 같으면
    if M == N:
        print(-1)
        continue
    
    # key 찾기(어떤 값을 기준으로 더해줄 것인지)
    if M > N:
        key = N # j = 1(i-j 최소 양수)
        if x > y: # 목표가 양수인 경우 -> 그대로 양수
            goal = x - y
        else: # 목표가 음수인 경우 -> 양수로 맞춰주기 위해 M 더해 줌
            goal = x + M - y
    else:
        key = M  # i = 1(i-j 음수)
        if x > y: # 목표가 양수인 경우 음수로 맞춰주기 위해 N 빼줌
            goal = x - N - y
        else:
            goal = x - y
    
    while True:
        i += key
        j += key
        
        if i > M:
            i -= M
        if j > N:
            j -= N
        
        year += key
        # 목표로 하는 차이에 도달한 경우
        if i - j == goal:
            # 원하는 차이만큼 더해주고 종료
            if i == 1:
                year += x - i
            else:
                year += y - j
            print(year)
            break
        
        # 초기화 된 경우(해를 못 찾은 경우)
        if i == 1 and j == 1:
            print(-1)
            break

# 빠르게 걸리는 코드
# 6064. 카잉 달력

# 1. 최소공배수까지 탐색한다.
# 2. 한 반복에 M씩 크기를 늘려 최대 반복횟수는 N(최대, 40000)

# import math

# # 입력 받기
# T = int(input())

# for _ in range(T):
#     M, N, x, y = map(int, input().split())
    
#     # 최소공배수 계산
#     gcd = math.gcd(M, N)    # 최대공약수를 구하고
#     lcm = M * N // gcd      # 최소공배수를 구함
    
#     found = 0               # 탐색 여부 변수
#     while x <= lcm:         # 최소공배수가 되기 전까지(끝 해에 도달하기 전까지)
#         if (x - 1) % N + 1 == y: # 식이 맞으면
#             print(x)        # 출력
#             found = 1  
#             break
#         x += M              # 좌측값을 기준으로 더해줌
    
#     if not found:           # 찾지 못한 경우 -1
#         print(-1)