# 수열 정의
def pado(n):
    arr = [0] * (n + 1)
    # 초기 값
    if n >= 1:
        arr[1] = 1
    if n >= 2:
        arr[2] = 1
    if n >= 3:
        arr[3] = 1
    # 수열
    for i in range(4, n + 1):
        arr[i] = arr[i-2] + arr[i-3]
    
    return arr[n]

T = int(input())
for test_case in range(T):    
    n = int(input())
    print(pado(n))
