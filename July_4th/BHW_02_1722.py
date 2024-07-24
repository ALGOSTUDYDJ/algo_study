# 1722. 순열의 순서

# 1. 순서의 순열을 맞춰야 하는 경우
# 1-1. 각 자릿수에서 수를 하나씩 증가시킴에 따라 순서를 빼가면서 진행한다.
# 1-2. 순서를 뺄 수 없는 경우 해당 자릿수에 들어갈 수는 해당 수이다.
# 1-3. 이를 N자릿수까지 반복한 후 순열을 출력한다.
# 2. 순열이 주어지면 순서를 맞춰야 하는 경우
# 2-1. 각 자릿수의 수까지 반복하며 각 자릿수까지의 순서를 더해갑며 진행한다.
# 2-2. 이를 N자릿수까지 반복한 후 순서를 출력한다.
# 3. 각 자릿수에서 더해지는 경우의 수는 팩토리얼에 해당한다.

import sys
input = sys.stdin.readline
N = int(input())    # 순열의 길이
F = [0]*(N + 1)  # 각 자리에서 만들 수 있는 순열의 갯수(팩토리얼)
S = [0]*(N + 1)  # 순열을 담는 리스트
visited = [0]*(N + 1)    # 숫자 사용 여부
F[0] = 1

# 팩토리얼 값을 이용한 초기화
for i in range(1, N + 1):   
    F[i] = F[i-1]*i
    
inputList = list(map(int, input().split()))

# 소문제 번호가 1이면(해당 순서의 순열을 맞춰야 하는 경우)
if inputList[0] == 1:   
    K = inputList[1]            # K는 순서
    for i in range(1, N + 1):   # 각 자릿수에 대해
        cnt = 1                 # 현재 순열에 들어갈 수가 몇 번째 순서의 수인가를 정하는 변수
        for j in range(1, N + 1): 
            # 앞선 자리에서 사용한 숫자일 경우 사용 불가
            # 순서를 증가시키지 않음(기존에 사용했기 때문에)
            if visited[j]:
                continue
            # 다음 수로 넘어갈 수 없는 경우
            # 현재 자리에 들어갈 숫자를 찾은 경우
            if K <= cnt*F[N-i]: 
                K -= (cnt - 1)*F[N-i]   # 해당하는 순서만큼 빼 줌
                S[i] = j                # 순열의 i번째 수 결정
                visited[j] = 1          # 사용 여부 표시
                break                   # 현재 순열 탐색 종료
            # 현재 순열에 들어갈 수의 순서 증가
            cnt += 1
    print(*S[1:])
# 소문제 번호가 2인 경우(순열이 주어지면 순서를 맞춰야 하는 경우)
else:
    K = 1   # 순서는 1번부터 시작
    for i in range(1, N + 1):               # 각 자리 수에 대해
        cnt = 0
        for j in range(1, inputList[i]):    # 순열의 해당 순서 수까지 탐색하며 
            # 해당 순서까지 순열의 앞 순서에서 사용되지 않은 미사용 수의 개수를 셈
            if not visited[j]:
                cnt += 1    
        # 순서는 해당 순서 경우의 수 * 해당 수에 도달하기까지 사용한 숫자의 수
        K += cnt * F[N-i]  
        visited[inputList[i]] = 1   # 사용 표시
    print(K)    # 순서 출력