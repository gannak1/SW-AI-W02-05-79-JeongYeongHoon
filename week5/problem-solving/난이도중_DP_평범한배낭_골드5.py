# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline
number_of_material, weight_limit = map(int, input().strip().split())

material = [(0, 0)]

for _ in range(number_of_material):
    m = tuple(map(int, input().strip().split()))
    material.append(m)

dp = {}
for w in range(weight_limit+1):
    if not dp.get(0):
        dp[0] = []
    dp[0].append(0)
max_value = 0
for m in range(1,len(material)):
    if not dp.get(m):
        dp[m] = []
        dp[m].append(0)
    for w in range(1,weight_limit + 1):
        weight = material[m][0]
        value = material[m][1]
        if w < weight:
            dp[m].append(dp[m-1][w])
        else:
            dp[m].append(max(dp[m-1][w-weight] + value, dp[m-1][w]))

max_value = dp[m][w]
print(max_value)

