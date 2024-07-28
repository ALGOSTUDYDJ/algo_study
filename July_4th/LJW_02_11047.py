n, k = map(int, input().split())  # 동전의 개수 n  금액 k
coins = [int(input()) for _ in range(n)]

# 정렬
coins.sort(reverse=True)  
cnt = 0  
for coin in coins:
    if k == 0:
        break   # 0이 되면 반복 종료
    if coin <= k:
        cnt += k // coin  
        k %= coin  

print(cnt)  
