# 수열의 길이 n, 수열 arr
n = int(input())
arr = list(map(int, input().split()))

# 수열 arr 의 원소 하나하나가 각각 부분수열의 맨마지막 원소가 됐을때 그 부분수열의 길이를 리스트에 기록합니다
# 가장 최소값은 자기자신 뿐인 1임

len_of_x=[1]*n


# 인덱스 0인 arr 은 1이기 때문에 생략함..(앞에 아무것도 없으니까)
# .......b....... < 인덱스 b 로 끝나는 부분수열 중에 제일 긴 길이 찾기
for b in range(1,n):
    for a in range(b): # b 앞에 있는 a 중에서
        end = arr[b]
        if arr[a] < arr[b] : # b 보다 작은 a 만 if 문으로 거른다 
            # len_of_x[b] = len_of_x[a]+1 # 그 a의 앞에 있는 부분수열의 개수를 통째로 b 앞에 놓을 부분수열로 가져온다..
            len_of_x[b] = max(len_of_x[a]+1, len_of_x[b]) # 여러 a 중에서 그중에 가장 길게 된 결과를 선택한다 
print(max(len_of_x))