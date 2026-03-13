# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

data_number = int(input())
compare_data = list(map(int, input().split()))
data_number = int(input())
check_data = list(map(int, input().split()))

result = [0] * len(check_data)

for i in range(len(check_data)):
    if check_data[i] in compare_data:
        result[i] = 1

for i in result:
    print(i)
