# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys
import math
import copy
input = sys.stdin.readline

rock_total, pass_rock_number = map(int,input().strip().split())
pass_rock = set()
for _ in range(pass_rock_number):
  pass_rock.add(int(input().strip()))

rock_road = [rock_total+1] * (rock_total)
# for i in pass_rock:
#   rock_road[i-1] = -1

# 2차원 DP
total_step = math.ceil((-1 + (1 + 8 * rock_total)  ** 0.5)/2)
dp = [copy.copy(rock_road) for _ in range(total_step)]
if rock_total == 1:
    print(0)
    sys.exit()
if 2 not in pass_rock:
  dp[0][1] = 1
for r in range(2,rock_total):
  for s in range(total_step):
    jump = s + 1
    if r+1 in pass_rock or jump > r:
      continue
    if s == 0:
      dp[s][r] = min(dp[s][r-jump],dp[s+1][r-jump]) + 1
    elif s == total_step-1:
      dp[s][r] = min(dp[s][r-jump],dp[s-1][r-jump]) + 1
    else:
      dp[s][r] = min(dp[s][r-jump],dp[s-1][r-jump],dp[s+1][r-jump]) + 1
min_step  = 99999999999
for s in range(total_step):
  if dp[s][-1] < rock_total and min_step > dp[s][-1]:
    min_step = dp[s][-1]
if min_step == 99999999999:
  min_step = -1
print(min_step)