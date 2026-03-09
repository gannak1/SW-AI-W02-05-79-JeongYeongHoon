# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

"""
for로 문자 반복
"""

input_range = int(input())
test_array = []
for i in range(input_range):
    z = input().split()
    z[0] = int(z[0])
    test_array.append(z)

for i in range(len(test_array)):
    number = test_array[i][0]
    word = test_array[i][1]
    print("".join([element * number for element in word]))
