# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import sys

data_list = list(map(int, sys.stdin.readline().rstrip("\n").split()))


def divide_conquer(data, pow_data,div_data):
    if pow_data == 1:
        return (data) % div_data
    elif pow_data % 2 == 0:
        half = divide_conquer(data, pow_data // 2,div_data)
        return (half * half) % div_data

    elif pow_data % 2 != 0:
            half = divide_conquer(data, (pow_data - 1) // 2,div_data)
            return (half * half * data) % div_data


print(divide_conquer(data_list[0], data_list[1], data_list[2]))
