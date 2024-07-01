# 14888. 연산자 끼워넣기


# 1. 연산자를 끼워넣는 모든 경우의 수에 대해 연산한다.
# 2. 각 경우의 수마다 연산 결과를 계산하여 연산의 최대와 최소를 갱신한다
# 3. 최종 연산 결과의 최대 최소를 출력한다.

N = int(input())    # 피연산자의 수

nums = list(map(int, input().split()))  # 피연산자
ops = list(map(int, input().split()))   # 4개의 연산자의 수

# 최대최소의 절댓값은 10억이라고 문제에 주어짐
minv = 1e9
maxv = -1e9

def dfs(n, now) :       # n : 현재 소모한 연산자의 수, now : 현재까지 연산의 결과
    global minv, maxv   # 최댓값과 최솟값 전역 선언
    
    # 종료 조건(모든 연산자 소진 시)
    if n == N-1:
        # 종료 시 수행될 연산(최대, 최소 갱신)
        minv = min(now, minv)      
        maxv = max(now, maxv)
        return

    # 남은 연산자들에 대해 연산 수행
    if ops[0] != 0 :    # 덧셈 연산자가 남은 경우
        ops[0] -= 1     # 연산자 소모
        dfs(n+1, now + nums[n+1])   # 연산 수행
        ops[0] += 1 

    if ops[1] != 0 : # 뺄셈 연산자가 남은 경우
        ops[1]-= 1  
        dfs(n+1, now - nums[n+1])
        ops[1] += 1
    
    if ops[2] != 0 : # 곱셈 연산자가 남은 경우
        ops[2] -= 1 
        dfs(n+1, now * nums[n+1])
        ops[2] += 1
    
    if ops[3] != 0 : #나눗셈 연산자가 남은 경우
        ops[3] -= 1 
        dfs(n+1, int(now/nums[n+1]))
        ops[3] += 1

dfs(0, nums[0])     # 연산 수행
print(maxv)         # 최댓값 출력
print(minv)         # 최솟값 출력