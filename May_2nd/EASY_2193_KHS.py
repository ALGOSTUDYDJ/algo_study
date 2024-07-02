
# 1로 시작한다.
# 1이 연속으로 나오지 않는다.
# N 자리의 이친수를 구해라.

# 먼저 실패한 방법입니다.

# 재귀로 풀어보도록 하자.
n = int(input()) # 이 친구는 깊이가 되겠지.

cnt = 0

for_what = [1]
def function1(depth):
    global cnt
    
    # 종료 조건
    if depth == n:
        cnt += 1
        return
    
    for i in range(2):
    # 앞에거를 비교해야한다. 만약 1이라면
        if i == for_what[depth - 1] == 1:
            continue
        else:
            # 기억했다가
            for_what.append(i)
            function1(depth + 1)
            # 까먹기
            for_what.pop()
            
# 1 넣고 시작했으니까 1번 했다 치고
function1(1)
print(cnt)



# 수정한 방법입니다.

# 규칙성을 찾으면 되는 문제
# 전전 인덱스 + 전 인덱스를 더하면 지금 인덱스 수

# 입력받기
n = int(input())

# dp arr 만들기
dp = [0] * (n + 1)
dp[1] = 1

# 규칙에 따른 반복문
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

# 출력
print(dp[n])
