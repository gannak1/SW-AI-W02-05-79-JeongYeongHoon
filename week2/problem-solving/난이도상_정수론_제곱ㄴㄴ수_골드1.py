# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016

import math

min_max_list = list(map(int, input().split()))  # 최대 최소값 인풋

total_array = [True] * (
    min_max_list[1] - min_max_list[0] + 1
)  # 에라토스테네스의 체 사용을 위한 준비, 소수값을 빠르게 찾기 위한 것

for i in range(2, int(math.sqrt(min_max_list[1])) + 1):

    start = (
        math.ceil(min_max_list[0] / (i**2)) * (i**2) - min_max_list[0]
    )  # 출발선, 처음 인덱싱할 숫자를 찾기 위해 최초 인풋값의 최소값에서 i 제곱을 나누 값에 올림 처리를 하고 i 제곱을 곱하고 최소값으로 빼서 처리

    for j in range(len(total_array)):
        if (
            len(total_array)
        ) <= start + i**2 * j:  # j의 인덱싱 값이 total_array의 크기보다 크면 종료하고 다음 소수 확인
            break
        total_array[start + j * i**2] = False


print(sum(total_array))  # 채에서 걸린 값들의 합으로 리턴
