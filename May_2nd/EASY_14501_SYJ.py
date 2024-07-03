def dfs(n, cost):
    global answer
    if n == N:  # 마지막 상담일에 다다랐을 경우
        answer = max(answer, cost)
        return
    if Ti[n] + n <= N:  # 현재 날짜 + 걸릴 상담 기간 <= 마지막 상담일
        dfs(n + Ti[n], cost + Pi[n])
    dfs(n+1, cost)  # 상담을 선택하지 않고 다음날로 넘길 때


N = int(input())
Ti, Pi = [], []     # Ti : 상담 걸리는 기간, Pi : 받을 수 있는 금액
for _ in range(N):
    ti, pi = map(int, input().split())
    Ti.append(ti)
    Pi.append(pi)
answer = 0
dfs(0, 0)
print(answer)