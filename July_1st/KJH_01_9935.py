# 백준 9935. 문자열 폭발

# 입력되는 문자열에, 폭발 문자열이 숨겨져있음
# 폭발 문자열은 폭발하며, 폭발하고 다시 이어진 문자열에 폭발 문자열이 있으면 다시 폭발
# 남은 문자열을 출력, 남은 문자열이 없는 경우 "FRULA" 출력

# 주어진 문자열의 각 문자를 순회하면서 stack에 추가
# 폭발 문자열의 길이만큼 스택의 끝 문자열을 검사해서, 폭발 문자열과 일치하면 pop으로 스택에서 꺼냄
# 순회 완료 후 스택에 문자가 남아있으면 이어붙여서 출력, 없는 경우 "FRULA" 출력

string = input()
target = list(input())
len_target = len(target)

stack = []

# 문자열을 순회하면서, 각 문자를 stack에 추가
for c in string:
    stack.append(c)
    # 매 번 슬라이싱으로 검사를 진행하면서, 끝 문자열이 폭발 문자열과 일치하면 stack에서 전부 pop 해준 뒤 다음 반복
    if stack[-len_target:] == target:
        for _ in range(len_target):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")