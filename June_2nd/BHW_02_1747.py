# 1747. 소수 & 팰린드롬


# 1. 소수가 아닌 수를 표시한다
# 2. 팰린드롬 수 여부를 판별하는 함수를 정의한다.
# 3. N부터 시작하여 소수인 수 중에 팰린드롬 수인지 여부를 판별하고 팰린드롬 수이면 출력한다.

N = int(input())

nums = [i for i in range(2000001)]  # 숫자 배열
nums[0] = 0 # 0과 1은 소수가 아님
nums[1] = 0

# 소수가 아닌 수 표시하기
for i in range(2, int(len(nums)**(1/2)) + 1):
    # 소수가 아니면 pass
    if nums[i] == 0:
        continue
    # 소수이면 해당 소수의 배수를 소수가 아닌 수로 표시
    for j in range(2*i, len(nums), i):
        nums[j] = 0

# 팰린드롬 판별함수
def isPalindrome(num):
    # 숫자를 문자열로 바꾼다
    string = list(str(num))
    # 시작 끝 인덱스를 지정한다
    s = 0
    e = len(string) - 1
    # 같은 위치에 있지 않을 때까지
    while s < e:
        # 두 수가 같지 않으면 팰린드롬 수가 아님
        if string[s] != string[e]:
            return False
        s += 1 
        e -= 1
    # while문이 정상 수행되었으면 True 반환
    return True

# N부터 숫자를 돌면서
for i in range(N, len(nums)):
    # 소수가 아니면 pass
    if nums[i] == 0:
        continue
    # 소수이면서 팰린드롬 수이면 출력 후 종료
    if (isPalindrome(nums[i])):
        print(nums[i])
        break