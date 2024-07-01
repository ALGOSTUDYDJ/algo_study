# 1105. 팔


# 1. 상한과 하한의 자릿수가 다르면 8의 최소 갯수는 0
# 2. 상한과 하한의 각 자릿수의 값이 다르면 그 이하 자리에서 8의 최소 갯수는 0
# 3. 상한과 하한의 각 자릿수의 값이 같고 그 값이 8이어야 최소 갯수 1 증가

L, R = map(int, input().split())
strL = list(str(L))
strR = list(str(R))

# 두 수의 자릿 수가 다르면 0
if len(strR) != len(strL):
    print(0)
else:   # 자릿수가 같으면
    cnt = 0                     # 8의 최소 갯수
    for i in range(len(strL)):  # 앞 자리부터 순회하면서 
        if strL[i] == strR[i]:  # 같은 자리의 수가 같은 경우
            # 그 값이 8인 경우 8의 최소 갯수 1 증가
            if strL[i] == '8':
                cnt += 1
            pass
        # 같은 자리의 수가 다른 경우
        else:
            break       # 그 이하 자릿수에서 8이 나타나는 횟수의 최소는 0
    print(cnt)