n = int(input())
arr = list(map(int, input().split()))
#dp 에 arr[i]를 마지막 선택했을시 가장 큰 증가 부분 수열의합
dp = arr[:]  # 각 요소를 마지막으로 선택했을 때의 가장 큰 증가 부분 수열의 합으로 초기화


for i in range(1, n):
    for j in range(i):
        # 현재 i의 값이 j보다 클때 dp[i] 갱신 (수열)
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))