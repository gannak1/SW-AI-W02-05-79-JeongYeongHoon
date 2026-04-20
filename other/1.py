# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline
column, row = list(map(int,input().strip().split(" ")))
array = []
for _ in range(column):
  array.append(list(input().strip()))
min_first_white = 99999999999999999
min_first_black = 99999999999999999
first_white = 0
first_black = 0
for k in range(column - 7):
  for l in range(row - 7):
    switch = False
    first_state = False
    first_white = 0
    first_black = 0
    for i in range(k,k+8):
      for j in range(l,l+8):
        if (array[i][j] != "B" and not switch):
          first_black += 1
        elif (array[i][j] != "W" and switch):
          first_black += 1
        if (array[i][j] != "W" and not switch):
          first_white += 1
        if (array[i][j] != "B" and switch):
          first_white += 1
        if (j == l + 7):
          switch = not first_state
          first_state = not first_state
        else:
          switch = not switch
    if (min_first_white > first_white):
      min_first_white = first_white
    if (min_first_black > first_black):
      min_first_black = first_black

print(min(min_first_white, min_first_black))