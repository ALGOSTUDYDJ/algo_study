# 11444. 피보나치 수 6

# 조건 : 1,000,000,000,000,000,000보다 작은 수

# 피보나치 수열 공식
# F_2n+1 = F_n+1^2 + F_n^2
# F_2n = (F_n-1 + F_n + 1)F_n = (2F_n-1 + F_n)F_n

from collections import defaultdict

## 피보나치 수열을 계산해주는 함수
def fibonacci(num):
  # 입력 수가 2 이하인 경우
  if num <= 2:
    return DP[num]
  # 해시 키 값이 존재하는 경우 해당 키에 존재하는 값을 반환해 중복 연산을 막음
  elif DP[num] > 0:
    return DP[num]
  # 키 값이 존재하지 않는 경우 최초 1회 연산을 진행
  # 공식 적용
  else :
    n = num //2 # K = 2n + 1 or K = 2n에서 n
    # 2의 배수인 경우
    if num % 2 == 0 :
      fn = fibonacci(n)
      fn_1 = fibonacci(n-1)
      DP[num] = ((2*fn_1 + fn)*fn)%1000000007
      return DP[num]
    # 2의 배수가 아닌 경우
    else : 
      fn_1 = fibonacci(n+1)
      fn = fibonacci(n)
      DP[num] = (fn_1**2 + fn**2)%1000000007
      return DP[num]
          

en = int(input())
DP = defaultdict(int) # 딕셔너리 초기화
DP[1],DP[2] = 1,1     # 초깃값 설정(1, 2번째 피보나치 수)

# 결과 출력
print(fibonacci(en))