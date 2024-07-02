# 수학 노잼

import math

# 입력 받기
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    # 최소공배수 계산 import gcd 썼습니다
    gcd = math.gcd(M, N)
    lcm = M * N // gcd
    
    found = 0 
    while x <= lcm:
        if (x - 1) % N + 1 == y:
            print(x)
            found = 1  
            break
        x += M
    
    if not found:
        print(-1)
