# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

"""
인풋을 받고 test_array로 받는다.
for 루프를 써서 각 test_array element array 의 값의 평균을 sum/len 로 구한 다음 count로 숫자를 셀 준비한다.
array의 element가 평균보다 크면 count += 1로 올려주고 count 값을 f-string으로 값을 불러온다.
"""

input_count = int(input())
test_array = [list(map(int, input().split()[1:])) for i in range(input_count)]


for i in range(len(test_array)):
    average = sum(test_array[i]) / len(test_array[i])
    count = 0
    for j in range(len(test_array[i])):
        if test_array[i][j] > average:
            count += 1
    print(f"{round(count / len(test_array[i]) * 100, 3)}%")
