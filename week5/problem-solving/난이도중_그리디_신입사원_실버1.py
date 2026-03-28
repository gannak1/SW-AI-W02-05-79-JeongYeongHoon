# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946


# def merge(arr, left, right):
#     mid = (left + right) // 2
#     left_arr = arr[left : mid + 1]
#     right_arr = arr[mid + 1 : right + 1]

#     i = 0
#     j = 0
#     left_arr.append([99999999999999, 99999999999999])
#     right_arr.append([99999999999999, 99999999999999])
#     for k in range(left, right + 1):
#         if left_arr[i][0] > right_arr[j][0]:
#             arr[k] = right_arr[j]
#             j += 1
#         else:
#             arr[k] = left_arr[i]
#             i += 1


# def merge_init(arr, left, right):
#     if left >= right:
#         return
#     mid = (left + right) // 2
#     merge_init(arr, left, mid)
#     merge_init(arr, mid + 1, right)
#     merge(arr, left, right)


# def start(arr):
#     if len(arr) == 1:
#         return arr
#     else:
#         merge_init(arr, 0, len(arr) - 1)
#         return arr


import sys

input = sys.stdin.readline
number_of_test = int(input().strip())
for _ in range(number_of_test):
    number_of_candidate = int(input().strip())
    candidate_list = []
    for _ in range(number_of_candidate):
        candidate_list.append(tuple(map(int, input().strip().split())))
    sorted_candidate_list = sorted(candidate_list)
    prev_candidate = sorted_candidate_list[0]
    success_number = 1
    for candidate_index in range(1,len(sorted_candidate_list)):
        candidate = sorted_candidate_list[candidate_index]
        if candidate[1] < prev_candidate[1]:
            prev_candidate = candidate
            success_number += 1
    print(success_number)