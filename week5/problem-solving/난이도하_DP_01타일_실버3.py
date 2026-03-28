# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys

tile_total_number = int(sys.stdin.readline().strip())


tile_number = 0
tile_status = {0:0,1:1,2:2}
number = [0,1,2]
number_index = 0

while tile_number <= tile_total_number and tile_total_number > 2:
    if tile_number == 0:
        tile_status[0] = 0
    elif tile_number == 1:
        tile_status[1] = 1
    elif tile_number == 2:
        tile_status[2] = 2
    else:
        tile_status[number[number_index]] = (((tile_status[number[number_index-1]])) + (tile_status[number[number_index-2]])) % 15746
        number_index = (number_index + 1) % 3

    tile_number += 1
if tile_total_number > 2:
    print(tile_status[number[number_index - 1]])
else:
    print(tile_total_number)