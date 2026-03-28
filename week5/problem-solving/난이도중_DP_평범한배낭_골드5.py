# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys

n = int(sys.stdin.readline().strip())

def fibo(n,memo=None):
    if memo == None:
        memo = {}
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    if memo.get(n):
        return memo.get(n)
    else:
        memo[n] = fibo(n-1,memo=memo) + fibo(n-2,memo=memo)
        return memo[n]
    
print(fibo(n))