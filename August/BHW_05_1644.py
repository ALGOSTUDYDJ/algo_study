# 1644. 소수의 연속합

# 1. 에라토스테네스 체의 방법을 이용해 소수를 구한다.
# 2. 해당 소수 배열로 연속합을 정해 N과 같은 경우의 수를 센다.
# 3. 해당 경우의 수를 출력한다.

N = int(input())  # 수 입력

# 소수 구하기
isPrimes = [1]*(N + 1)  # 해당 수까지의 소수 여부 배열 생성
isPrimes[0] = 0
isPrimes[1] = 0
primes = [] # 소수 배열

for i in range(N + 1):
  # 소수인지 판별이 안 된 수(즉, 소수)에 대해서만
  if isPrimes[i]:
    primes.append(i)  # 소수 배열에 추가
    # 해당 수의 배수들의 소수 여부를 False로 변경
    for j in range(2*i, N+1, i):
      isPrimes[j] = 0 

# 소수의 연속합
l, r = 0, 0 # 좌우 포인터
total = 0   # 누적합
cnt = 0     # 연속합 개수

while r < len(primes):
  # 연속합이 N인 경우 개수 증가 및 좌, 우측 포인터 이동
  if total == N:
    cnt += 1 
    total -= primes[l] 
    total += primes[r]
    l += 1
    r += 1
  # N보다 큰 경우 좌측 포인터 이동
  elif total > N:
    total -= primes[l]
    l += 1
  # N보다 작은 경우 우측 포인터 이동
  else:
    total += primes[r]
    r += 1

# 마지막 좌측 포인터 이동
while l < r:
  if total == N:
    cnt += 1
    break
  elif total < N:
    break
  else:
    total -= primes[l]
    l += 1

print(cnt)