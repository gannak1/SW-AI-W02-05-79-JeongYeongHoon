# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

test_case_number = int(input)
for _ in range(test_case_number):
  coin_number = int(input())
  coin_list = list(map(int,input().strip().split()))
  total = int(input())
  