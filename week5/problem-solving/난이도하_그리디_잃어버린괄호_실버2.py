# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline
text_split_minus = input().strip().split("-")

return_number = 0

is_plus = True

for i,value in enumerate(text_split_minus):
    if is_plus:
        return_number += sum(list(map(int,value.split("+"))))
    else:
        return_number -= sum(list(map(int,value.split("+"))))
    if i == 0:
        is_plus = not is_plus
print(return_number)