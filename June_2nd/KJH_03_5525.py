# 5525_IOIOI

# N, M, S 입력
N = int(input())
M = int(input())
S = input()

# S 안의 PN의 갯수 cnt 변수 선언
cnt = 0
# 문자열의 인덱스로 사용할 정수 변수 선언
idx = 0

# 인덱스를 사용한 반복 I - OI를 연속으로 찾을 때 인덱스를 두 개씩 밀얼주기 위해 while문 사용
while idx < M - 2:

    # idx 번째 문자부터 idx + 2 번째까지 (연달아 3개) 확인
    if S[idx:idx + 3] == 'IOI':
        j = 0

        # IOI로 확인됟면 맨 처음 I를 뗀 OI의 개수를 세어줌 (PN이 I + OI * N 이므로)
        while idx + 2 < M and S[idx+1:idx+3] == 'OI':
            # OI가 확인되면 연달아 반복된 OI의 갯수를 j에 더해주고, idx에 2를 더해 다음 OI 확인
            idx += 2
            j += 1
            # 만약 PN이 만들어지면, 결과에 1을 더해주고 맨 앞의 IO를 떼준다는 개념으로 j에서 1을 빼줌
            if j == N:
                cnt += 1
                j -= 1
    # IOI가 아니면 다음 문자 검사
    else:
        idx += 1

print(cnt)