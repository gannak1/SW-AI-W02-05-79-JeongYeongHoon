# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys

input_number = int(sys.stdin.readlines().rstrip("\n"))
data = [int(sys.stdin.readlines().rstrip("\n")) for _ in range(input_number)]

data.sort()
