N = int(input())
M = int(input())
S = input()



length = 2 * N + 1

# Pn 패턴을 찾기 
cnt = 0
i = 0

while i <= M - length:
    if S[i] == 'I':
        match_cnt = 0
        while i + 1 < M and S[i + 1] == 'O' and i + 2 < M and S[i + 2] == 'I':
            match_cnt += 1
            i += 2
            if match_cnt == N:
                cnt += 1
                match_cnt -= 1
        i += 1
    else:
        i += 1

print(cnt)