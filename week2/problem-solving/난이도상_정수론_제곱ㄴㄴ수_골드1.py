# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016

import math

min_max_list = list(map(int, input().split()))

count = 0

total_array = [True] * (min_max_list[1] - min_max_list[0] + 1)

for i in range(2, int(math.sqrt(min_max_list[1])) + 1):

    start = math.ceil(min_max_list[0] / (i**2)) * (i**2) - min_max_list[0]

    for j in range(len(total_array)):
        if (len(total_array)) <= start + i**2 * j:
            break
        total_array[start + j * i**2] = False


print(sum(total_array))
