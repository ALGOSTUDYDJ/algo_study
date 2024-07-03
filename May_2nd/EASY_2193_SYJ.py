# - n=2, 10
# - n=3, 10+[0,1] =>[100,101]
# - n=4, 10+[00,01,10] => [1000,1001,1010]
# - n=4일때, n=3 숫자(뒤에서 2자리) 2개, n=2의 1개의 숫자의 조합
# - 따라서 길이 n인 이친수 dp[n]=dp[n-2]+dp[n-1]
# = answer[n-1] + answer[n-2]

n = int(input())

if n == 1 or n == 2:
    print(1)
else:
    answer = [0]*(n+1)
    answer[1] = 1
    answer[2] = 1

    for i in range(3, n+1):
        answer[i] = answer[i-1] + answer[i-2]
    print(answer[n])