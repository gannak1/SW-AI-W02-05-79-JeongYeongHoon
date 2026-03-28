# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline
count, change = list(map(int,input().strip().split()))
coin_data = [int(input().strip()) for _ in range(count)]

total_coin = 0
coin_counting = {}


while change > 0:
    for coin_index in range(len(coin_data)-1,-1,-1):
        if change >= coin_data[coin_index]:
            coin = coin_data[coin_index]
            coin_counting[coin] = (change // coin)
            total_coin += (change // coin)
            change -= (change // coin) * coin
            break
print(total_coin)